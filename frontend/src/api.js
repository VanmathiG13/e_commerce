// src/api.js
 // Update path as necessary

import axios from 'axios';

const API_URL = 'http://localhost:3000/api/; // Adjust the URL if need'



export const fetchCategories = async () => {
    try {
        const response = await axios.get('http://127.0.0.1:8000/api/categories/');
        return response.data; // Ensure this returns the correct data format
    } catch (error) {
        console.error("Error fetching categories:", error);
        throw error; // Rethrow for handling in the component
    }
};




export const fetchProducts = async () => {
    try {
        const response = await axios.get('http://127.0.0.1:8000/api/products/');
        return response.data; // Ensure this returns the correct data format
    } catch (error) {
        console.error("Error fetching products:", error);
        throw error; // Rethrow for handling in the component
    }
};


export const fetchProductsByCategory = async (categoryId) => {
    try {
        const response = await axios.get(`http://127.0.0.1:8000/api/products/category/${categoryId}/`);
        return response.data; // Adjust based on your API response structure
    } catch (error) {
        console.error("Error fetching products by category:", error);
        throw error;
    }
};

