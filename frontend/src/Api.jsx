export const API_URL = 'https://api-service-dlp9.onrender.com' || 'http://localhost:8000';

export const fetchBookings = async () => {
    try {
        const response = await fetch(`${API_URL}/bookings/`);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    } catch (error) {
        console.error('Error fetching bookings:', error);
        throw error;
    }
};
