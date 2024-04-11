import Header from "./Header";
import { useState, useEffect } from "react";
import { Outlet, useNavigate } from "react-router-dom";
import NavBar from "./NavBar";

function App() {
  const [hotels, setHotels] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    fetch("/hotels")
      .then((res) => res.json())
      .then((hotelData) => setHotels(hotelData));
  }, []);

  function addHotel(newHotel) {
    fetch("/hotels", {
      method: "POST",
      headers: {
        "Content-type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify(newHotel),
    }).then((res) => {
      if (res.ok) {
        res.json().then((newHotelData) => setHotels([...hotels, newHotelData]));
        navigate("/");
      } else {
        res.json().then((errorData) => alert(`Error:${errorData.error}`));
      }
    });
  }

  function updateHotel(id, hotelDataForUpdate, setHotelFromHotelProfile) {
    fetch(`/hotels/${id}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "Application/JSON",
        Accept: "application/json",
      },
      body: JSON.stringify(hotelDataForUpdate),
    }).then((res) => {
      if (res.ok) {
        res.json().then((updatedHotelData) => {
          setHotelFromHotelProfile(updatedHotelData);
          setHotels((hotels) =>
            hotels.map((hotel) => {
              if (hotel.id == updatedHotelData.id) {
                return updatedHotelData;
              }
            })
          );
        });
      } else if (res.status == 404 || res.status == 400) {
        res.json().then((errorData) => alert(`Error: ${errorData.error}`));
      }
    });
  }

  function deleteHotel(id) {
    fetch(`/hotels/${id}`, {
      method: "DELETE",
    }).then((res) => {
      if (res.ok) {
        setHotels((hotels) =>
          hotels.filter((hotel) => {
            return hotel.id !== id;
          })
        );
      } else if (res.status === 404) {
        res.json().then((errorData) => alert(`Error: ${errorData.error}`));
      }
    });
  }

  return (
    <div className="app">
      <NavBar />
      <Header />
      <Outlet
        context={{
          hotels: hotels,
          addHotel: addHotel,
          deleteHotel: deleteHotel,
          updateHotel: updateHotel,
        }}
      />
    </div>
  );
}

export default App;
