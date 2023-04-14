import "./App.css";
import { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [search, setSearch] = useState("");
  const [allData, setAllData] = useState({
    city: "",
    country: "",
    temperature: "",
    humidity: "",
    minTemperature: "",
    weatherIcons: "",
  });

  useEffect(() => {
    // we add what we want to happen after rending
    // --> fetch the DB
    fetchData();
  }, []);

  const fetchData = async (city) => {
    try {
      const APIKEY = "6c2bb102977fb085dce057619ea59995";
      const result = await axios.get(
        `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${APIKEY}&units=metric`
      );
      await setAllData({
        city: result.data.name,
        country: result.data.sys.country,
        temperature: result.data.main.temp,
        humidity: result.data.main.humidity,
        minTemperature: result.data.main.temp_min,
        weatherIcons: result.data.weather.icon,
      });
    } catch (e) {
      console.log("API not loaded correctly");
    }
  };

  const handleSubmit = (e) => {
    console.log(search);
    fetchData(search);
    e.preventDefault();
  };

  const handleChange = (e) => {
    setSearch(e.target.value);
  };

  return (
    <main>
      <div className="App">
        <form onSubmit={handleSubmit}>
          <input
            value={search}
            type="text"
            name="city"
            placeholder="CITY NAME IS..."
            onChange={handleChange}
          />
          <button htmlFor="city"></button>
        </form>
        <section>
          <h1>{allData.city}</h1>
          <h2>{allData.country}</h2>

          <div>
            <h3>TEMPERATURE</h3>
            <p>{allData.temperature}</p>
            <p>{allData.minTemperature}</p>
          </div>
          <div>
            <h4>HUMIDITY</h4>
            <p>{allData.humidity}</p>
          </div>
        </section>
      </div>
    </main>
  );
}

export default App;
