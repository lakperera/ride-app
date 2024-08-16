"use client";
import React from "react";

const TopBar = () => {
  return (
    <div className="grid gap-4 p-4 lg:grid-cols-5">
      <div className="flex justify-between w-full col-span-1 p-4 bg-white border rounded-lg lg:col-span-2">
        <div className="flex flex-col w-full pb-4">
          <p className="text-2xl font-bold">$7,846</p>
          <p className="text-gray-600">Daily Revenue</p>
        </div>
        <p className="flex items-center justify-center p-2 bg-green-200 rounded-lg">
          <span className="text-lg text-green-700">+18%</span>
        </p>
      </div>
      <div className="flex justify-between w-full col-span-1 p-4 bg-white border rounded-lg lg:col-span-2">
        <div className="flex flex-col w-full pb-4">
          <p className="text-2xl font-bold">$1,437,876</p>
          <p className="text-gray-600">YTD Revenue</p>
        </div>
        <p className="flex items-center justify-center p-2 bg-green-200 rounded-lg">
          <span className="text-lg text-green-700">+11%</span>
        </p>
      </div>
      <div className="flex justify-between w-full p-4 bg-white border rounded-lg">
        <div className="flex flex-col w-full pb-4">
          <p className="text-2xl font-bold">11,437</p>
          <p className="text-gray-600">Customers</p>
        </div>
        <p className="flex items-center justify-center p-2 bg-green-200 rounded-lg">
          <span className="text-lg text-green-700">+17%</span>
        </p>
      </div>
    </div>
  );
};

export default TopBar;
