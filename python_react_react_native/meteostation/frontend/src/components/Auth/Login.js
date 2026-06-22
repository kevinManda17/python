import React, { useState } from "react";
import api from "../../api/api";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await api.post("token/", { username, password });
      localStorage.setItem("access", res.data.access);
      navigate("/dashboard");
    } catch {
      alert("Erreur d'authentification");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Nom d'utilisateur" />
      <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Mot de passe" />
      <button type="submit">Connexion</button>
    </form>
  );
};

export default Login;


