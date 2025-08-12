const API_URL = 'http://localhost:8000/bookings/';

export const fetchBookings = async () => {
    try {
        console.log('Fetching bookings from:', API_URL);
        const response = await fetch(API_URL);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    } catch (error) {
        console.error('Error fetching bookings:', error);
        throw error;
    }
};
