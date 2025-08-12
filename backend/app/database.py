from sqlalchemy import create_engine, Column, Integer, String, Date, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import enum
from .schemas import Room_Type, Hotel_Name

DATABASE_URL = "postgresql://user:password@localhost:5432/hotel_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Booking(Base):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True, index=True)
    guest_name = Column(String, index=True)
    room_type = Column(Enum(Room_Type), nullable=False)
    hotel_name = Column(Enum(Hotel_Name), nullable=False)
    price_per_night = Column(Integer)
    check_in_date = Column(Date)
    check_out_date = Column(Date)
