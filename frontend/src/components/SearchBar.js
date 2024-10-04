import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const SearchBar = () => {
    const [searchTerm, setSearchTerm] = useState('');
    const navigate = useNavigate();

    const handleSearch = async (e) => {
        e.preventDefault();

        try {
            const response = await fetch(`http://127.0.0.1:8000/search/?search=${searchTerm}`);
            const data = await response.json();
            navigate('/search', {
                state: { searchResults: data.results, searchQuery: searchTerm }
            });
        } catch (error) {
            console.error('Error fetching search results:', error);
        }
    };

    return (
        <form onSubmit={handleSearch}>
            <input
                type="text"
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                placeholder="Search for products..."
            />
            <button type="submit">Search</button>
        </form>
    );
};

export default SearchBar;
