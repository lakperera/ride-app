"use client";
import React from "react";
import { FaShoppingBag } from "react-icons/fa";
import { BsThreeDotsVertical } from "react-icons/bs";
import { data } from "../data/data";

const orders = () => {

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
  return (
    <div className="min-h-screen bg-gray-100">
      <div className="flex justify-between px-4 pt-4">
        <h2>Orders</h2>
        <h2>Welcome Back, Clint</h2>
      </div>
      <div className="p-4">
        <div className="w-full p-4 m-auto overflow-y-auto bg-white border rounded-lg">
          <div className="grid items-center justify-between grid-cols-2 p-2 my-3 cursor-pointer md:grid-cols-4 sm:grid-cols-3">
            <span>Order</span>
            <span className="text-right sm:text-left">Status</span>
            <span className="hidden md:grid">Last Order</span>
            <span className="hidden sm:grid">Method</span>
          </div>
          <ul>
            {data.map((order, id) => (
              <li
                key={id}
                className="grid items-center justify-between grid-cols-2 p-2 my-3 rounded-lg cursor-pointer bg-gray-50 hover:bg-gray-100 md:grid-cols-4 sm:grid-cols-3"
              >
                <div className="flex">
                  <div className="p-3 bg-purple-100 rounded-lg">
                    <FaShoppingBag className="text-purple-800" />
                  </div>
                  <div className="pl-4">
                    <p className="font-bold text-gray-800">
                      ${order.total.toLocaleString()}
                    </p>
                    <p className="text-sm text-gray-800">{order.name.first}</p>
                  </div>
                </div>
                <p className="text-right text-gray-600 sm:text-left">
                  <span
                    className={
                      order.status == "Processing"
                        ? "bg-green-200 p-2 rounded-lg"
                        : order.status == "Completed"
                        ? "bg-blue-200 p-2 rounded-lg"
                        : "bg-yellow-200 p-2 rounded-lg"
                    }
                  >
                    {order.status}
                  </span>
                </p>
                <p className="hidden md:flex">{order.date}</p>
                <div className="items-center justify-between hidden sm:flex">
                  <p>{order.method}</p>
                  <BsThreeDotsVertical />
                </div>
              </li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
};

export default orders;
