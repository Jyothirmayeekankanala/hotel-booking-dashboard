from faker import Faker
from random import randint, choice
from datetime import timedelta
from app import database
from sqlalchemy.orm import Session

fake = Faker()

def generate_fake_bookings(db: Session, n = 150):
    for _ in range(n):
        room_types = list(database.Room_Type)
        check_in_date = fake.date_between(start_date='-30d', end_date='today')
        booking = database.Booking(
            guest_name=fake.name(),
            hotel_name=choice(list(database.Hotel_Name)),
            room_type=choice(room_types),
            price_per_night=randint(70, 250)*10,
            check_in_date=check_in_date,
            check_out_date=check_in_date + timedelta(days=randint(1, 5))
        )
        db.add(booking)
        db.commit()
