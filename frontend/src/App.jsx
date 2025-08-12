import { useState, useEffect } from 'react'
import {fetchBookings} from './Api'
import Bookings from './components/Bookings'
import BookingsOverTime from './components/BookingsOverTime'
import RoomTypeStatistics from './components/RoomTypeStatistics'
import RevenueStatistics from './components/RevenueStatistics'
import BookingsStatistics from './components/BookingsStatistics'

function App() {
  const [bookings, setBookings] = useState([])

  useEffect(() => {
    fetchBookings().then((data) => {
      setBookings(data)
  })
  }, [])
  return (
    <>
      <BookingsOverTime bookings={bookings} />
      <RoomTypeStatistics bookings={bookings} />
      <RevenueStatistics bookings={bookings} />
      <BookingsStatistics bookings={bookings} />
      <Bookings bookings={bookings} />
    </>
  )
}

export default App
