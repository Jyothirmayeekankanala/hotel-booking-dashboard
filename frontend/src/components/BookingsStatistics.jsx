import { useEffect, useState } from "react";
import {API_URL} from '../Api';

export default function Bookings({ bookings }) {
    const [info, setInfo] = useState({})
        useEffect(() => {
        fetch(`${API_URL}/bookings-stats/`)
            .then((response) => response.json())
            .then((data) => {
                setInfo(data);
            });
    }, []);

    return (
        <div className="bookings">
            <p>Total Bookings: {info.total_bookings}</p>
            <p>Total Revenue: ${info.total_revenue}</p>
            {info.total_bookings > 0 && (
                <>
                    <h3>Room Type Distribution:</h3>
                    <ul>
                        {Object.entries(info.room_type_counts).map(([roomType, count]) => (
                            <li key={roomType}>{roomType}: {count}</li>
                        ))}
                    </ul>
                </>
            )}
        </div>
    );
}