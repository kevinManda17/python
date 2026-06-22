import React, { useContext } from "react";
import { ThemeContext } from "../context/ThemeProvider";

const ThemeToggle = () => {
  const { mode, setMode } = useContext(ThemeContext);

  return (
    <div>
      <button onClick={() => setMode("light")}>Clair</button>
      <button onClick={() => setMode("dark")}>Sombre</button>
      <button onClick={() => setMode("auto")}>Auto</button>
      <p>Thème actuel : {mode}</p>
    </div>
  );
};

export default ThemeToggle;
