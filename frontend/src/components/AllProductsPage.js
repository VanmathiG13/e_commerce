import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { fetchProducts, fetchCategories } from '../api';

const ITEMS_PER_PAGE = 6;

const AllProductsPage = () => {
    const [products, setProducts] = useState([]);
    const [categories, setCategories] = useState([]);
    const [selectedCategory, setSelectedCategory] = useState('');
    const [searchTerm, setSearchTerm] = useState('');
    const [currentPage, setCurrentPage] = useState(1);
    const navigate = useNavigate();

    // Fetch products and categories
    useEffect(() => {
        const getData = async () => {
            try {
                const productData = await fetchProducts();
                setProducts(productData);
                const categoryData = await fetchCategories();
                setCategories(categoryData);
            } catch (error) {
                console.error("Error fetching data:", error);
            }
        };
        getData();
    }, []);

    // Filter products by search term and selected category
    const filteredProducts = products.filter(product => {
        const matchesSearchTerm = product.product_name.toLowerCase().includes(searchTerm.toLowerCase());
        const matchesCategory = selectedCategory === '' || product.category.category_name === selectedCategory;

        // Debugging: log the product category and selected category
        console.log(`Product: ${product.product_name}, Category: ${product.category.category_name}, Selected: ${selectedCategory}`);

        return matchesSearchTerm && matchesCategory;
    });

    const totalPages = Math.ceil(filteredProducts.length / ITEMS_PER_PAGE);
    const startIndex = (currentPage - 1) * ITEMS_PER_PAGE;
    const selectedProducts = filteredProducts.slice(startIndex, startIndex + ITEMS_PER_PAGE);

    const handlePageChange = (page) => {
        setCurrentPage(page);
    };

    const handleSearchSubmit = (e) => {
        e.preventDefault();
        if (searchTerm.trim()) {
            navigate(`/search?q=${encodeURIComponent(searchTerm)}`); // Redirect to search results
        }
    };

    const handleCategoryChange = (e) => {
        setSelectedCategory(e.target.value);
        setCurrentPage(1); // Reset to first page when category is changed
    };

    const renderPagination = () => {
        const pages = [];
    
        pages.push(
            <button
                key={1}
                onClick={() => handlePageChange(1)}
                className={`btn ${currentPage === 1 ? 'btn-primary' : 'btn-light'} mx-1`}
            >
                1
            </button>
        );

        if (currentPage > 3) {
            pages.push(<span key="ellipsis1" className="mx-1">...</span>);
        }

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

        if (currentPage < totalPages - 2) {
            pages.push(<span key="ellipsis2" className="mx-1">...</span>);
        }

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
        <div className="container" style={{ marginTop: '20px' }}>
            <h2 className="text-center mb-4">All Products</h2>

            {/* Filter by Category */}
            <div className="row mb-4">
                <div className="col-md-4">
                    <label htmlFor="categoryFilter" className="form-label">Filter by Category</label>
                    <select 
                        id="categoryFilter" 
                        className="form-select" 
                        value={selectedCategory} 
                        onChange={handleCategoryChange}
                    >
                        <option value="">All Categories</option>
                        {categories.map(category => (
                            <option key={category.category_id} value={category.category_name}>
                                {category.category_name}
                            </option>
                        ))}
                    </select>
                </div>
            </div>

            {/* Products List */}
            <div className="row">
                {selectedProducts.map(product => (
                    <div key={product.product_id} className="col-md-4 mb-4">
                        <div className="card">
                            <img src={product.image_url} alt={product.product_name} className="card-img-top" />
                            <div className="card-body">
                                <h5 className="card-title">{product.product_name}</h5>
                                <p className="card-text">{product.description}</p>
                                <p className="card-text">
                                    <small className="text-muted">MRP: ${product.mrp}</small><br />
                                    <small className="text-muted">Discounted Price: ${product.discounted_price}</small><br />
                                    <small className="text-muted">Available: {product.product_count}</small>
                                </p>
                            </div>
                        </div>
                    </div>
                ))}
            </div>

            {/* Pagination Controls */}
            <div className="pagination-controls text-center mt-4">
                {renderPagination()}
            </div>
        </div>
    );
};

export default AllProductsPage;
