// frontend/script.js

// Example JavaScript logic to interact with Flask backend API

const apiUrl = 'http://your-flask-api-url/api';

// Function to fetch data from the Flask API
async function fetchData() {
    try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
    }
}

// Call fetchData() to retrieve data
fetchData();
