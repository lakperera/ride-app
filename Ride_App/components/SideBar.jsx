"use client";
import Link from "next/link";
import React, { useState } from "react";;
import { AiOutlineMenu, AiOutlineClose } from "react-icons/ai";
import { FaCar,FaBootstrap ,FaUserGroup,FaPersonBreastfeeding,FaAngleDown  ,    } from "react-icons/fa6";
import { FaSignOutAlt } from "react-icons/fa";
import { HiMenuAlt2 } from "react-icons/hi";
import { VscReport } from "react-icons/vsc";
import { IoIosSettings } from "react-icons/io";
import { FcFeedback } from "react-icons/fc";
import { SiKnowledgebase } from "react-icons/si";
import { MdBrowserUpdated } from "react-icons/md";
import { CgProfile } from "react-icons/cg";


const SideBar = ({ children }) => {
  const [isOpen, setIsOpen] = useState(false);
  const [isDropDownList ,setdropDownList] = useState(false);

  const handleToggle = () => {
    setIsOpen(!isOpen);
  };

  const handleDropDown = () => {
    setdropDownList(!isDropDownList);
  }

  return (
    <div className='flex'> 
    <div className={` flex ${isOpen ? 'w-0 md:w-64' : 'w-20 xl:0'}`}>
        <button className={` fixed text-white cursor-pointer togglebutton top-2 ${isOpen ? 'togglebutton' : 'togglebuttonClose'}`} onClick={handleToggle}><HiMenuAlt2 className='flex-row-reverse h-10 w-14'/></button>
        {/* Sidebar */}
        <div
          className={`navigation z-50 flex flex-col items-center`}
        >
          <ul >
                <li className="pointer-events-none">
                    <Link href="#" id="logoname">
                        <span class="icon">
                            <img src="" alt="logo" />
                        </span>
                        <span class="title">Company Name</span>
                        
                    </Link>
                    
                </li>
                  <li>
                      <Link href="/">
                          <span class="icon">
                          <FaCar className="w-8 h-8 m-2 ml-6"/>
                          </span>
                          <span class="title">Dispatch</span>
                      </Link>
                  </li>
                <li>
                    <Link href="/order">
                        <span class="icon">
                        <FaBootstrap className="w-8 h-8 m-2 ml-6"/>
                        </span>
                        <span class="title">Booking</span>
                    </Link>
                </li>

                <li>
                    <Link href="#">
                        <span class="icon">
                            <VscReport className="w-8 h-8 m-2 ml-6"/>
                        </span>
                        <span class="title">Reports</span>
                    </Link>
                </li>

                <li>
                  <div className="flex">
                  <Link href="#" >
                            <span class="icon">
                            <FaUserGroup className="w-8 h-8 m-2 ml-6"/>
                            </span>
                            <span class="title">Users
                            </span>
                </Link>
                <button onClick={()=>handleDropDown((prev) => !prev)} className="hover:text-black"><FaAngleDown className="mt-4 mr-4 text-white hover:text-black"/></button>
                  </div>
                
                  {isDropDownList && 
                        <ul className="relative ml-20">
                                <li className="pointer-events-auto">
                                  <Link href="#">
                                    <span className="title">Passengers</span>
                                  </Link>
                                </li>
                                <li>
                                  <Link href="/drivers">
                                    <span className="title">Drivers</span>
                                  </Link>
                                </li>
                                <li>
                                  <Link href="#">
                                    <span className="title">Fleet Operators</span>
                                  </Link>
                                </li>
                                <li>
                                  <Link href="#">
                                    <span className="title">Admins</span>
                                  </Link>
                                </li>
                                <li>
                                  <Link href="#">
                                    <span className="title">Deletion Request</span>
                                  </Link>
                                </li>
                        </ul>
                  }
                </li>

                <li>
                    <Link href="#">
                        <span class="icon">
                            <FcFeedback className="w-8 h-8 m-2 ml-6" />
                        </span>
                        <span class="title">Feedback</span>
                    </Link>
                </li>

                <li>
                    <Link href="#">
                        <span class="icon">
                          <IoIosSettings className="w-8 h-8 m-2 ml-6"/>
                        </span>
                        <span class="title">Settings</span>
                    </Link>
                </li>
                
                <li>
                    <Link href="#">
                        <span class="icon">
                          <SiKnowledgebase className="w-8 h-8 m-2 ml-6"/>
                        </span>
                        <span class="title">Knowledge Base</span>
                    </Link>
                </li>
                <li>
                    <Link href="#">
                        <span class="icon">
                          <MdBrowserUpdated className="w-8 h-8 m-2 ml-6"/>
                        </span>
                        <span class="title">Updates</span>
                    </Link>
                </li>
                <li>
                    <Link href="#">
                        <span class="icon">
                          <CgProfile className="w-8 h-8 m-2 ml-6"/>
                        </span>
                        <span class="title">Profile</span>
                    </Link>
                </li>


                <li>
                    <Link href="#">
                        <span class="icon">
                        <FaSignOutAlt className="w-8 h-8 m-2 ml-6 "  />
                        </span>
                        <span class="title">Sign Out</span>
                    </Link>
                </li>
          </ul>
        </div>
        
      {/* Main content */}
    </div>
      <main className="flex-1 m-0 md:m-0">{children}</main>
    </div>
  );
};

export default SideBar;
