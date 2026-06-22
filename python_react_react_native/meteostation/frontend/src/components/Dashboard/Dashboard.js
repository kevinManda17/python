import React, { useEffect, useState } from "react";
import api from "../../api/api";

const Dashboard = () => {
  const [stations, setStations] = useState([]);
  const [readings, setReadings] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const token = localStorage.getItem("access");
        const config = { headers: { Authorization: `Bearer ${token}` } };
        const stationsRes = await api.get("stations/", config);
        const readingsRes = await api.get("readings/", config);
        setStations(stationsRes.data);
        setReadings(readingsRes.data);
      } catch {
        console.error("Erreur de chargement des données");
      }
    };
    fetchData();
  }, []);

  return (
    <div>
      <h2>Stations</h2>
      <pre>{JSON.stringify(stations, null, 2)}</pre>
      <h2>Mesures</h2>
      <pre>{JSON.stringify(readings, null, 2)}</pre>
    </div>
  );
};

export default Dashboard;
