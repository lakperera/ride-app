
import React, { useState } from 'react';
import { useRouter } from 'next/router';
import axios from 'axios';
import Link from 'next/link';
const dropDown =()=>{
  console.log("clik")
}

const Header = () => {


  const [profiledrop, setProfileDrop] = useState(false);
  const [isLoggedOut, setIsLoggedOut] = useState(false); 
  const [isOpen, setIsOpen] = useState(false)

  const logoutSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://127.0.0.1:8000/api/logout");
      if (response.data.message === "successful") {
        console.log("Successfully logged out");
        setIsLoggedOut(true); // Set logout status to true
      }
    } catch (e) {
      console.error(e);
    }
  };

  if (isLoggedOut) {
    // Redirect to home if logged out successfully
    window.location.href = "/";
  }

  return (

    // <div className="flex justify-between px-4 py-4 md:bg-gradient-to-r from-indigo-100">
      
    //   <h2 className="self-center text-xl">DashBoard</h2>
    //   {/* <div className="flex" >
    //     <button><svg onClick={()=>setProfileDrop((prev) => !prev)} className="w-10 mx-5 rounded-md cursor-pointer " xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" id="profile"><path fill="#2b2e63" d="M32 0C14.4 0 0 14.4 0 32s14.4 32 32 32c17.7 0 32-14.4 32-32S49.7 0 32 0zm0 62.1C15.4 62.1 1.9 48.6 1.9 32S15.4 1.9 32 1.9 62.1 15.4 62.1 32 48.6 62.1 32 62.1z"></path><path fill="#ededed" d="M32 1.9C15.4 1.9 1.9 15.4 1.9 32S15.4 62.1 32 62.1 62.1 48.6 62.1 32 48.6 1.9 32 1.9zm0 10.8c4.8 0 8.8 3.9 8.8 8.8 0 4.8-3.9 8.8-8.8 8.8-4.8 0-8.8-3.9-8.8-8.8.1-4.8 4-8.8 8.8-8.8zm15.9 37.7H16.1c-.5 0-1-.4-1-1 0-9.3 7.6-16.9 16.9-16.9 9.3 0 16.9 7.6 16.9 16.9 0 .6-.4 1-1 1z"></path><path fill="#d6d6d6" d="M32 1.9C15.4 1.9 1.9 15.4 1.9 32S15.4 62.1 32 62.1 62.1 48.6 62.1 32 48.6 1.9 32 1.9zm0 58.2C16.5 60.1 3.9 47.5 3.9 32S16.5 3.9 32 3.9 60.1 16.5 60.1 32 47.5 60.1 32 60.1z"></path><path fill="#2b2e63" d="M32 32.5c-9.3 0-16.9 7.6-16.9 16.9 0 .5.4 1 1 1H48c.5 0 1-.4 1-1-.1-9.3-7.7-16.9-17-16.9zm-14.9 16c.5-7.8 7-14 14.9-14s14.4 6.2 14.9 14H17.1z"></path><path fill="#f26e61" d="M46.9 48.5H17.1c.5-7.8 7-14 14.9-14s14.4 6.2 14.9 14z"></path><path fill="#2b2e63" d="M32 12.7c-4.8 0-8.8 3.9-8.8 8.8 0 4.8 3.9 8.8 8.8 8.8 4.8 0 8.8-3.9 8.8-8.8 0-4.8-4-8.8-8.8-8.8zm0 15.6c-3.8 0-6.8-3-6.8-6.8s3.1-6.8 6.8-6.8c3.8 0 6.8 3.1 6.8 6.8s-3 6.8-6.8 6.8z"></path><path fill="#ffe5ab" d="M38.8 21.5c0 3.8-3.1 6.8-6.8 6.8-3.8 0-6.8-3-6.8-6.8s3.1-6.8 6.8-6.8c3.8 0 6.8 3 6.8 6.8z"></path><path fill="#e15e5a" d="M32 34.5c-7.9 0-14.4 6.2-14.9 14H47c-.6-7.8-7.1-14-15-14zm0 1.5c6.5 0 12.1 4.7 13.2 11H18.8c1.1-6.3 6.7-11 13.2-11z"></path><path fill="#f0d39a" d="M32 14.7c-3.8 0-6.8 3.1-6.8 6.8s3.1 6.8 6.8 6.8c3.8 0 6.8-3 6.8-6.8s-3-6.8-6.8-6.8zm0 12.1c-2.9 0-5.3-2.4-5.3-5.3s2.4-5.3 5.3-5.3 5.3 2.4 5.3 5.3-2.4 5.3-5.3 5.3z"></path></svg></button> 
    //     {profiledrop && <div className="flex flex-col dropdownProfile">
    //       <ul className="flex flex-col gap-4 ">
    //         <li><a  href="#">Profile</a></li>
    //         <li><button onClick={logoutSubmit}>LogOut</button></li>
    //         <li><a href='/login'>Login</a></li>
    //       </ul>
    //     </div>}
        
    //     <h2 className="self-center">Welcome Back, User</h2>
    //   </div> */}
      
    // </div>
    <div class="flex justify-between px-4 py-4 bg-blue-950">
    <div class="self-center ">
      </div>

    <div class="search">
        <label>
            <input type="text" placeholder="Search here"/>
            <ion-icon name="search-outline"></ion-icon>
        </label>
    </div>

    <div className="flex" >
    <button><svg onClick={()=>setProfileDrop((prev) => !prev)} className="w-10 mx-5 rounded-md cursor-pointer " xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" id="profile"><path fill="#2b2e63" d="M32 0C14.4 0 0 14.4 0 32s14.4 32 32 32c17.7 0 32-14.4 32-32S49.7 0 32 0zm0 62.1C15.4 62.1 1.9 48.6 1.9 32S15.4 1.9 32 1.9 62.1 15.4 62.1 32 48.6 62.1 32 62.1z"></path><path fill="#ededed" d="M32 1.9C15.4 1.9 1.9 15.4 1.9 32S15.4 62.1 32 62.1 62.1 48.6 62.1 32 48.6 1.9 32 1.9zm0 10.8c4.8 0 8.8 3.9 8.8 8.8 0 4.8-3.9 8.8-8.8 8.8-4.8 0-8.8-3.9-8.8-8.8.1-4.8 4-8.8 8.8-8.8zm15.9 37.7H16.1c-.5 0-1-.4-1-1 0-9.3 7.6-16.9 16.9-16.9 9.3 0 16.9 7.6 16.9 16.9 0 .6-.4 1-1 1z"></path><path fill="#d6d6d6" d="M32 1.9C15.4 1.9 1.9 15.4 1.9 32S15.4 62.1 32 62.1 62.1 48.6 62.1 32 48.6 1.9 32 1.9zm0 58.2C16.5 60.1 3.9 47.5 3.9 32S16.5 3.9 32 3.9 60.1 16.5 60.1 32 47.5 60.1 32 60.1z"></path><path fill="#2b2e63" d="M32 32.5c-9.3 0-16.9 7.6-16.9 16.9 0 .5.4 1 1 1H48c.5 0 1-.4 1-1-.1-9.3-7.7-16.9-17-16.9zm-14.9 16c.5-7.8 7-14 14.9-14s14.4 6.2 14.9 14H17.1z"></path><path fill="#f26e61" d="M46.9 48.5H17.1c.5-7.8 7-14 14.9-14s14.4 6.2 14.9 14z"></path><path fill="#2b2e63" d="M32 12.7c-4.8 0-8.8 3.9-8.8 8.8 0 4.8 3.9 8.8 8.8 8.8 4.8 0 8.8-3.9 8.8-8.8 0-4.8-4-8.8-8.8-8.8zm0 15.6c-3.8 0-6.8-3-6.8-6.8s3.1-6.8 6.8-6.8c3.8 0 6.8 3.1 6.8 6.8s-3 6.8-6.8 6.8z"></path><path fill="#ffe5ab" d="M38.8 21.5c0 3.8-3.1 6.8-6.8 6.8-3.8 0-6.8-3-6.8-6.8s3.1-6.8 6.8-6.8c3.8 0 6.8 3 6.8 6.8z"></path><path fill="#e15e5a" d="M32 34.5c-7.9 0-14.4 6.2-14.9 14H47c-.6-7.8-7.1-14-15-14zm0 1.5c6.5 0 12.1 4.7 13.2 11H18.8c1.1-6.3 6.7-11 13.2-11z"></path><path fill="#f0d39a" d="M32 14.7c-3.8 0-6.8 3.1-6.8 6.8s3.1 6.8 6.8 6.8c3.8 0 6.8-3 6.8-6.8s-3-6.8-6.8-6.8zm0 12.1c-2.9 0-5.3-2.4-5.3-5.3s2.4-5.3 5.3-5.3 5.3 2.4 5.3 5.3-2.4 5.3-5.3 5.3z"></path></svg></button> 
    {profiledrop && <div className="flex flex-col dropdownProfile">
      <ul className="flex flex-col gap-4 ">
        <li><a  href="#">Profile</a></li>
        <li><button onClick={logoutSubmit}>LogOut</button></li>
        <li><Link href='/login'>Login</Link></li>
      </ul>
    </div>}

<h2 className="self-center">Welcome Back, User</h2>
</div>
    </div>
  );
};

export default Header;




