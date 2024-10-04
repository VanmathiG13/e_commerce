// src/firebase-config.js
import { initializeApp } from 'firebase/app';
import { getAuth } from 'firebase/auth';

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyBDOhS_aXcgJH1yGovg8Zl5ytDE-7gs1pg",
    authDomain: "e-commerce-5a6dc.firebaseapp.com",
    projectId: "e-commerce-5a6dc",
    storageBucket: "e-commerce-5a6dc.appspot.com",
    messagingSenderId: "472142246888",
    appId: "1:472142246888:web:82a9b1f835a7df16236a5d",
    measurementId: "G-B41443D2LH"
  };

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

export { auth };
