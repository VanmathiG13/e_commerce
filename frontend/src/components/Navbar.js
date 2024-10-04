import React from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import { FaShoppingCart } from 'react-icons/fa';
import SearchBar from './SearchBar'; // Import the SearchBar component

const Navbar = () => {
    const location = useLocation();
    const navigate = useNavigate();

    // Don't show the navbar on the '/' and '/signup' routes
    if (location.pathname === '/' || location.pathname === '/signup') {
        return null;
    }

    // Logout function to clear any user data and redirect to home page
    const handleLogout = () => {
        // Perform any logout actions here, such as clearing authentication tokens
        // For now, we can just redirect to the home page
        navigate('/');
    };

    return (
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <div className="container-fluid">
                <Link className="navbar-brand">
                    <FaShoppingCart size={30} />
                </Link>
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarNav">
                    <ul className="navbar-nav me-auto">
                        <li className="nav-item">
                            <Link className="nav-link" to="/category">Categories</Link>
                        </li>
                        <li className="nav-item">
                            <Link className="nav-link" to="/all-products">All Products</Link>
                        </li>
                    </ul>
                    {/* Insert Search Bar */}
                    <SearchBar />
                    <button 
                        className="btn btn-outline-danger ms-3"
                        onClick={handleLogout}
                    >
                        Logout
                    </button>
                </div>
            </div>
        </nav>
    );
};

export default Navbar;
