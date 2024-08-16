import React, { useEffect } from "react";
import { useRouter } from "next/router";
import axios from "axios";

const CookiesValidation = () => {
  const router = useRouter();
  useEffect(() => {
    const validateCookie = async () => {
      const token = localStorage.getItem("token");

      if (!token) {
        // If no token is found, redirect to the home page or handle as needed
        router.push("/");
        return;
      }

      try {
        const response = await axios.post(
          "http://127.0.0.1:8000/api/validation",
          { token }
        );

        if (response.data.message === "success") {
          console.log("Validation successful");
          router.push("/setting");
        } else {
          console.log("Validation failed");
          router.push("/");
        }
      } catch (error) {
        console.error("Error during validation:", error);
        router.push("/");
      }
    };

    validateCookie();
  }, [router]);

  return null; // Or return a loading spinner, etc.
};

export default CookiesValidation;
