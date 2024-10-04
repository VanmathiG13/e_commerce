import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { fetchProducts } from '../api'; // Adjust the import as necessary

const ProductPage = () => {
  const { categoryId } = useParams(); // Get categoryId from the URL
  const [products, setProducts] = useState([]);
  const [filteredProducts, setFilteredProducts] = useState([]);
  const [searchTerm, setSearchTerm] = useState(''); // State for search term

  useEffect(() => {
    const getProducts = async () => {
      try {
        const data = await fetchProducts(); // Fetch all products
        setProducts(data);

        // Filter products by category ID
        const filtered = data.filter(product => product.category.category_id === parseInt(categoryId));
        setFilteredProducts(filtered);
      } catch (error) {
        console.error("Error fetching products:", error);
      }
    };

    getProducts();
  }, [categoryId]);

  // Filter products based on the search term
  const handleSearch = (e) => {
    setSearchTerm(e.target.value);

    const filtered = products.filter(product => 
      (product.category.category_id === parseInt(categoryId)) && 
      (product.product_name.toLowerCase().includes(e.target.value.toLowerCase()) ||
      product.description.toLowerCase().includes(e.target.value.toLowerCase()))
    );
    setFilteredProducts(filtered);
  };

  return (
    <div className="container" style={{ marginTop: '20px' }}>
      <h2 className="text-center mb-4">Products in Category {categoryId}</h2>

      {/* Search bar */}
      <div className="input-group mb-4">
        <input
          type="text"
          className="form-control"
          placeholder="Search products..."
          value={searchTerm}
          onChange={handleSearch}
        />
      </div>

      {/* Products List */}
      <div className="row">
        {filteredProducts.length > 0 ? (
          filteredProducts.map(product => (
            <div className="col-md-4 text-center mb-4" key={product.product_id}>
              <div className="card shadow-sm" style={{ borderRadius: '10px' }}>
                <img 
                  src={product.image_url} 
                  className="card-img-top" 
                  alt={product.product_name} 
                  style={{ borderTopLeftRadius: '10px', borderTopRightRadius: '10px', height: '150px', width: '100%', objectFit: 'cover' }} 
                />
                <div className="card-body">
                  <h5 className="card-title">{product.product_name}</h5>
                  <p className="card-text">MRP: ${product.mrp}</p>
                  <p className="card-text">Discount Price: ${product.discounted_price}</p>
                  <p className="card-text">Stock: {product.product_count}</p>
                </div>
              </div>
            </div>
          ))
        ) : (
          <div className="col-12 text-center">
            <p>No products found for this category.</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default ProductPage;
