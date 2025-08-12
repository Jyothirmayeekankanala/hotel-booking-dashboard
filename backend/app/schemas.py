from pydantic import BaseModel
from datetime import date
from enum import Enum, IntEnum
class Room_Type(str, Enum):
    SINGLE = "Single"
    DOUBLE = "Double"
    SUITE = "Suite"
    DELUXE = "Deluxe"

class Hotel_Name(str, Enum):
    JACYS_HOTEL = "Jacys Hotel"
    ESSOESS_HOTEL = "Essoess Hotel"
    ELLERYBEACHHOUSE = "Ellery Beach House"
    HOMEOFESS = "Home of Ess"
    FYRIRESORT = "Fyri Resort"
    FALKENBERGSTRANDBAD = "Falkenberg Strandbad"
    MARIENLYSTSTANDHOTEL = "Marienlyst Strandhotel"
    STEAMHOTEL = "Steam Hotel"
    YSTADSALTSJÖBAD = "Ystad Saltsjöbad"
    MJS_HOTEL = "MJS Hotel"
    HOTELPIGALLE = "Hotel Pigalle"
    HOTELBELLORA = "Hotel Bellora"
    VILLASTRANDVÄGEN = "Villa Strandvägen"
    MARYHILLESTATE = "Maryhill Estate"
    HJORTVIKENCOUNTRYCLUB = "Hjortviken Country Club"
    ROXRESORT = "Rox Resort"
    KOKPUNKTEN = "Kokpunkten"
    ZAMENHOF = "Zamenhof"
    CHERILEEGOTHENBURG = "Cheri-lee Gothenburg"
    PORTDUSOLEIL = "Port du Soleil"
    EIGHT = "8ight"
    VILLAJOHANNEBERG    = "Villa Johanneberg"
    VILLAODINSLUND = "Villa Odinslund"
    TRANQUILO = "Tranquilo"
    BARABICUE = "Barabicu"

class BookingBase(BaseModel):
    guest_name: str
    hotel_name: Hotel_Name
    room_type: Room_Type
    price_per_night: int
    check_in_date: date
    check_out_date: date

class BookingCreate(BookingBase):
    pass 

class Booking(BookingBase):
    id: int

    class Config:
        orm_mode = True