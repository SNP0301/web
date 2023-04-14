import "./App.css";
import { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [allData, setAllData] = useState({
    city: "atlanta",
    country: "",
    temperature: "",
  });

  useEffect(() => {
    // we add what we want to happen after rending
    // --> fetch the DB
    fetchData();
  }, []);

  const fetchData = async (city) => {
    const APIKEY = "6c2bb102977fb085dce057619ea59995";
    const result = await axios.get(
      `https://api.openweathermap.org/data/2.5/weather?q=${"atlanta"}&appid=${APIKEY}`
    );
    await setAllData({
      city: result,
      country: result.data.sys.country,
      temperature: result.data.main.temp,
    });
  };

  return (
    <div className="App">{console.log("keep focus", allData.country)}</div>
  );
}

export default App;
