import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const SignUpForm = () => {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
  });

  const navigate = useNavigate();

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Form submitted:', formData);
    navigate('/', { state: { email: formData.email, password: formData.password } });
  };

  const handleSignInRedirect = () => {
    navigate('/'); // Redirect to Home page
  };

  return (
    <div className="container" style={{ marginTop: '50px', padding: '0 20%' }}>
      <form onSubmit={handleSubmit} style={{ padding: '20px', backgroundColor: '#f8f9fa', borderRadius: '0.5rem', boxShadow: '0 0.5rem 1rem rgba(0,0,0,0.1)' }}>
        <h3 className="text-center mb-4">Sign Up</h3>
        
        <div className="mb-3">
          <label htmlFor="username" className="form-label">Username</label>
          <input
            type="text"
            className="form-control"
            id="username"
            name="username"
            value={formData.username}
            onChange={handleChange}
            required
            autoComplete="off" // Disable autofill
            style={{ borderRadius: '0.25rem', borderColor: '#ced4da' }}
          />
        </div>
        <div className="mb-3">
          <label htmlFor="email" className="form-label">Email address</label>
          <input
            type="email"
            className="form-control"
            id="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            required
            autoComplete="off" // Disable autofill
            style={{ borderRadius: '0.25rem', borderColor: '#ced4da' }}
          />
        </div>
        <div className="mb-3">
          <label htmlFor="password" className="form-label">Password</label>
          <input
            type="password"
            className="form-control"
            id="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
            required
            autoComplete="off" // Disable autofill
            style={{ borderRadius: '0.25rem', borderColor: '#ced4da' }}
          />
        </div>
        <button type="submit" className="btn btn-primary w-100" style={{ borderRadius: '0.25rem' }}>Sign Up</button>

        <div className="text-center mt-3">
          <p>
            Already have an account?{' '}
            <button
              className="btn btn-link"
              onClick={handleSignInRedirect}
              style={{ padding: '0', textDecoration: 'none' }}
            >
              Sign In
            </button>
          </p>
        </div>
      </form>
    </div>
  );
};

export default SignUpForm;
