import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import { ThemeProvider } from "./context/ThemeProvider";
import Login from "./components/Auth/Login";
import Register from "./components/Auth/Register";
import Dashboard from "./components/Dashboard/Dashboard";
import ThemeToggle from "./components/ThemeToggle";

function App() {
  return (
    <ThemeProvider>
      <Router>
        <header style={{ marginBottom: "1rem" }}>
          <nav style={{ display: "flex", gap: "1rem" }}>
            <Link to="/">Connexion</Link>
            <Link to="/register">Inscription</Link>
            <Link to="/dashboard">Dashboard</Link>
          </nav>
          <ThemeToggle />
        </header>

        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/dashboard" element={<Dashboard />} />
        </Routes>
      </Router>
    </ThemeProvider>
  );
}

export default App;
