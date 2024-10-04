import React, { useState, useEffect } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';

const LoginForm = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const location = useLocation();
  const { state } = location;
  const navigate = useNavigate();

  useEffect(() => {
    if (state && state.email && state.password) {
      setEmail(state.email);
      setPassword(state.password);
    }
  }, [state]);

  const handleLogin = (e) => {
    e.preventDefault();
    console.log('Logging in with', email, password);
    navigate('/category');
  };

  return (
    <form onSubmit={handleLogin}>
      <div className="form-group mb-3">
        <label>Email</label>
        <input
          type="email"
          className="form-control"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
          autoComplete="off" // Disable autofill
        />
      </div>
      <div className="form-group mb-3">
        <label>Password</label>
        <input
          type="password"
          className="form-control"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
          autoComplete="off" // Disable autofill
        />
      </div>
      <button type="submit" className="btn btn-primary w-100">Sign In</button>
    </form>
  );
};

export default LoginForm;
