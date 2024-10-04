import React, { useState } from 'react';
import firebaseConfig from '../firebase-config'; // If it's in the src directory
// Adjust the path as necessary
import { auth } from '../firebase-config'; // Adjust the path as necessary

import { getAuth, signInWithPopup, GoogleAuthProvider } from 'firebase/auth';
import SignUpForm from './SignUpForm';
import LoginForm from './LoginForm';
import { useNavigate } from 'react-router-dom';


const Home = () => {
  const navigate = useNavigate();
  const [isSignUp, setIsSignUp] = useState(false);

  const toggleForm = () => {
    navigate('/signup');
  };

  const handleGoogleSignIn = async () => {
    const provider = new GoogleAuthProvider();
    try {
      const result = await signInWithPopup(auth, provider);
      const user = result.user;
      console.log('User signed in:', user);
      navigate('/category');
      // Redirect to category page after sign-in
      // Implement your redirect logic here
    } catch (error) {
      console.error('Error signing in with Google:', error);
    }
  };

  return (
    <div className="container" style={{ marginTop: '50px' }}>
      <div className="row justify-content-center">
        <div className="col-md-6">
          <div className="card shadow">
            <div className="card-body">
              <h3 className="text-center mb-4">
                {isSignUp ? 'Sign Up' : 'Sign In'}
              </h3>

              {isSignUp ? (
                <SignUpForm />
              ) : (
                <LoginForm />
              )}

              <div className="text-center mt-3">
                {isSignUp ? (
                  <p>
                    Already have an account?{' '}
                    <button
                      className="btn btn-link"
                      onClick={toggleForm}
                      style={{ padding: '0', textDecoration: 'none' }}
                    >
                      Sign In
                    </button>
                  </p>
                ) : (
                  <p>
                    Don't have an account?{' '}
                    <button
                      className="btn btn-link"
                      onClick={toggleForm}
                      style={{ padding: '0', textDecoration: 'none' }}
                    >
                      Sign Up
                    </button>
                  </p>
                )}
              </div>

              <div className="text-center mt-4">
                <button 
                  className="btn btn-danger w-100" 
                  onClick={handleGoogleSignIn}
                >
                  Sign in with Google
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home;
