import React, { useEffect } from 'react';
import { useLocation } from 'react-router-dom';

const SearchResults = () => {
    const location = useLocation();
    const { searchResults = [], searchQuery = '' } = location.state || {};

    useEffect(() => {
        console.log('Search Query:', searchQuery);
        console.log('Search Results:', searchResults);
    }, [searchResults, searchQuery]);

    return (
        <div className="container mt-4">
            <h1>Search Results for "{searchQuery}"</h1>
            {searchResults.length > 0 ? (
                <ul className="list-group">
                    {searchResults.map((product, index) => (
                        <li key={`${product.id}-${index}`} className="list-group-item">
                            <h2>{product.product_name}</h2>
                            <p>{product.description}</p>
                            <p><strong>MRP:</strong> ${Number(product.mrp).toFixed(2)}</p>
                            <p><strong>Discounted Price:</strong> ${Number(product.discounted_price).toFixed(2)}</p>
                            <img src={product.image_url} alt={product.product_name} className="img-fluid" />
                        </li>
                    ))}
                </ul>
            ) : (
                <p>No results found.</p>
            )}
        </div>
    );
};

export default SearchResults;
