import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, useLocation } from 'react-router-dom';
import Home from './components/Home';
import CategoryPage from './components/CategoryPage';
import AllProductsPage from './components/AllProductsPage';
import ProductPage from './components/ProductPage';
import SearchResults from './components/SearchResults'; // Import SearchResults
import 'bootstrap/dist/css/bootstrap.min.css';
import SignUp from './components/SignUpForm';
import Navbar from './components/Navbar'; // Import Navbar

const App = () => {
  const [showWelcome, setShowWelcome] = useState(false);
  const [username, setUsername] = useState('');

  const handleProfileClick = () => {
    setShowWelcome((prev) => !prev); // Toggle welcome message
  };

  const location = useLocation();

  return (
    <>
      {/* Render Navbar for all routes except "/" and "/signup" */}
      {location.pathname !== '/' && location.pathname !== '/signup' && (
        <Navbar handleProfileClick={handleProfileClick} />
      )}

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/category" element={<CategoryPage />} />
        <Route path="/all-products" element={<AllProductsPage />} />
        <Route path="/products/category/:categoryId" element={<ProductPage />} />
        <Route path="/search" element={<SearchResults />} /> {/* Use query parameter */}
        <Route path="/signup" element={<SignUp />} />
      </Routes>
    </>
  );
};

export default App;
