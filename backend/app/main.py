from . import database, schemas
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import func
from sqlalchemy.orm import Session
from . import fake_data_seeding
from datetime import date

# database.Base.metadata.drop_all(database.engine)
database.Base.metadata.create_all(database.engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def read_root():
    return {"message": "Welcome to the Hotel Booking API"}

@app.post('/bookings/create-booking')
def create_booking(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    data = booking.dict()
    data['room_type'] = booking.room_type.value
    db_booking = database.Booking(**data)
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

@app.post('/bookings/seed-fake-data/')
def create_fake_bookings(count: int = 150, db: Session = Depends(get_db)):
    fake_data_seeding.generate_fake_bookings(db, count)
    return {"message": "Fake bookings created"}

@app.get('/bookings/')
def get_bookings(db: Session = Depends(get_db)):
    bookings = db.query(database.Booking).all()
    return bookings

@app.get('/bookings/filter/')
def get_filtered_bookings(start_date: date,
    end_date: date,
    room_type: str = None,
    db: Session = Depends(get_db)):
    query = db.query(database.Booking).filter(database.Booking.check_in_date >= start_date,
                                               database.Booking.check_out_date <= end_date)
    if room_type:
        query = query.filter(database.Booking.room_type == room_type)
    bookings = query.all()
    return bookings

@app.get('/bookings-stats/')
def get_bookings_statistics(db: Session = Depends(get_db)):
    total_bookings = db.query(database.Booking).count()
    total_revenue = db.query(func.sum(database.Booking.price_per_night)).scalar() or 0

    room_type_counts = db.query(
        database.Booking.room_type,
        func.count(database.Booking.room_type).label("count")
    ).group_by(database.Booking.room_type).all()

    return {
        "total_bookings": total_bookings,
        "total_revenue": total_revenue,
        "room_type_counts": {room_type: count for room_type, count in room_type_counts}
    }

@app.get('/room-type-stats/')
def get_room_type_statistics(db: Session = Depends(get_db)):
    room_type_counts = db.query(
        database.Booking.room_type,
        func.count(database.Booking.room_type).label("count")
    ).group_by(database.Booking.room_type).all()

    return [{"name": str(room_type), "count": count} for room_type, count in room_type_counts]

@app.get('/bookings-over-time/')
def get_bookings_over_time(db: Session = Depends(get_db)):
    bookingsOverTime = db.query(database.Booking.check_in_date, func.count(database.Booking.id).label("count")
    ).group_by(database.Booking.check_in_date).order_by(database.Booking.check_in_date).all()

    return [{"date": str(check_in_date), "count": count} for check_in_date, count in bookingsOverTime]

@app.get('/revenue-over-time/')
def get_revenue_over_time(db: Session = Depends(get_db)):
    revenueOverTime = db.query(
        database.Booking.check_in_date,
        func.sum(database.Booking.price_per_night).label("total_revenue")
    ).group_by(database.Booking.check_in_date).order_by(database.Booking.check_in_date).all()

    return [{"date": str(check_in_date), "total_revenue": total_revenue} for check_in_date, total_revenue in revenueOverTime]


#optional endpoints
@app.get('/bookings/{booking_id}')
def get_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = db.query(database.Booking).filter(database.Booking.id == booking_id).first()
    if not booking:
        return {"error": "Booking not found"}
    return booking