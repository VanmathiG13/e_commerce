import React, { useState, useEffect } from 'react';
import { fetchCategories } from '../api'; // Importing fetchCategories
import { useNavigate, useLocation } from 'react-router-dom';

const CategoryPage = () => {
    const [categories, setCategories] = useState([]);
    const [currentPage, setCurrentPage] = useState(1); // Track the current page
    const [categoriesPerPage] = useState(6); // Number of categories per page
    const [username, setUsername] = useState('');
    const [showWelcome, setShowWelcome] = useState(false);
    
    const location = useLocation();
    const navigate = useNavigate();

    // Retrieve username from the location state
    useEffect(() => {
        if (location.state && location.state.username) {
            setUsername(location.state.username);
        }
    }, [location.state]);

    useEffect(() => {
        const getCategories = async () => {
            try {
                const data = await fetchCategories();
                setCategories(data);
            } catch (error) {
                console.error("Error fetching categories:", error);
            }
        };
        getCategories();
    }, []);

    const handleCategoryClick = (categoryId) => {
        navigate(`/products/category/${categoryId}`);
    };

    // Handle pagination logic
    const indexOfLastCategory = currentPage * categoriesPerPage;
    const indexOfFirstCategory = indexOfLastCategory - categoriesPerPage;
    const currentCategories = categories.slice(indexOfFirstCategory, indexOfLastCategory);

    const totalPages = Math.ceil(categories.length / categoriesPerPage);

    const handlePageChange = (pageNumber) => {
        setCurrentPage(pageNumber);
    };

    // Render pagination buttons
    const renderPagination = () => {
        const pages = [];

        // Always show the first page
        pages.push(
            <button
                key={1}
                onClick={() => handlePageChange(1)}
                className={`btn ${currentPage === 1 ? 'btn-primary' : 'btn-light'} mx-1`}
            >
                1
            </button>
        );

        // Show ellipsis if needed
        if (currentPage > 3) {
            pages.push(<span key="ellipsis1" className="mx-1">...</span>);
        }

        // Show current page and surrounding pages
        const startPage = Math.max(2, currentPage - 1);
        const endPage = Math.min(totalPages - 1, currentPage + 1);

        for (let i = startPage; i <= endPage; i++) {
            pages.push(
                <button
                    key={i}
                    onClick={() => handlePageChange(i)}
                    className={`btn ${currentPage === i ? 'btn-primary' : 'btn-light'} mx-1`}
                >
                    {i}
                </button>
            );
        }

        // Show ellipsis if needed
        if (currentPage < totalPages - 2) {
            pages.push(<span key="ellipsis2" className="mx-1">...</span>);
        }

        // Always show the last page
        if (totalPages > 1) {
            pages.push(
                <button
                    key={totalPages}
                    onClick={() => handlePageChange(totalPages)}
                    className={`btn ${currentPage === totalPages ? 'btn-primary' : 'btn-light'} mx-1`}
                >
                    {totalPages}
                </button>
            );
        }

        return pages;
    };

    return (
        <div className="container mt-5">
            <h2 className="text-center mb-4">Categories</h2>
            <div className="row">
                {currentCategories.length > 0 ? (
                    currentCategories.map((category) => (
                        <div className="col-md-4 mb-4" key={category.category_id}>
                            <div className="card h-100 shadow-sm">
                                <img src={category.image_url} className="card-img-top" alt={category.category_name} />
                                <div className="card-body">
                                    <h5 className="card-title">{category.category_name}</h5>
                                    <button 
                                        className="btn btn-primary"
                                        onClick={() => handleCategoryClick(category.category_id)}>
                                        View Products
                                    </button>
                                </div>
                            </div>
                        </div>
                    ))
                ) : (
                    <div className="col-12 text-center">
                        <p>No categories available.</p>
                    </div>
                )}
            </div>
            <div className="d-flex justify-content-center mt-4">
                {renderPagination()}
            </div>
        </div>
    );
};

export default CategoryPage;
