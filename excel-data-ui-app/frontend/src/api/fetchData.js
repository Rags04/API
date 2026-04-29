import axios from 'axios';

const API_URL = 'http://localhost:5000/api/data'; // Adjust the URL as needed

export const fetchData = async () => {
    try {
        const response = await axios.get(API_URL);
        return response.data;
    } catch (error) {
        console.error('Error fetching data:', error);
        throw error; // Rethrow the error for further handling
    }
};