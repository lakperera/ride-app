"use client";
import { useRouter } from 'next/router';
import { useState } from 'react';
import axios from 'axios';
import Link from 'next/link';
import { data } from 'autoprefixer';

export const LoginPage = () => {
  const router = useRouter();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  


  const SetCookies = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/login', { email, password });

      // get data from server and store it in the local storage and check if it 
      if (response.data.message === 'success') {
        localStorage.setItem("token" , response.data.jwt);
        router.push('/');
      }
    } catch (error) {
      alert('Wrong details');
      console.error(error);
    }
  };

  return (
    <div className="bg-white LoginBody">
      <div className="wrapper">
        <form method="POST" onSubmit={SetCookies} className='context'>
          <h1>Login</h1>
          <div className="input-box">
            <input
              name="email"
              type="email"
              placeholder="Email"
              onChange={(e) => setEmail(e.target.value)}
              required
            />
            <i className="bx bxs-user"></i>
          </div>
          <div className="input-box">
            <input
              name="password"
              type="password"
              placeholder="Password"
              onChange={(e) => setPassword(e.target.value)}
              required
            />
            <i className="bx bxs-lock-alt"></i>
          </div>
          <div className="remember-forgot">
            <label>
              <input type="checkbox" />
              Remember me
            </label>
            <a href="#">Forgot password?</a>
          </div>
          <button type="submit" className="btn" onClick={SetCookies}>
            Login
          </button>
        </form>
      </div>
    </div>
  );
};

export default LoginPage;
