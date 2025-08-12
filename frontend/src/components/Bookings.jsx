
export default function BookingsTable({ bookings }) {
    return (
        <div className="bookings">
            <h2>Bookings:</h2>
            <table>
                <thead>
          <tr>
            <th>Guest Name</th>
            <th>Hotel Name</th>
            <th>Room Type</th>
            <th>Price per Night</th>
            <th>Check-in Date</th>
            <th>Check-out Date</th>
          </tr>
        </thead>
        <tbody>
          {bookings.map((booking) => (
            <tr key={booking.id}>
              <td>{booking.guest_name}</td>
              <td>{booking.hotel_name}</td>
              <td>{booking.room_type}</td>
              <td>${booking.price_per_night}</td>
              <td>{new Date(booking.check_in_date).toLocaleDateString()}</td>
              <td>{new Date(booking.check_out_date).toLocaleDateString()}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}