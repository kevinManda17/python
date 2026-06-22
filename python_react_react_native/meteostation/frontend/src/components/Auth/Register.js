import React, { useState } from "react";
import api from "../../api/api";
import { useNavigate } from "react-router-dom";

const Register = () => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [password2, setPassword2] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (password !== password2) {
      alert("Les mots de passe ne correspondent pas !");
      return;
    }

    try {
      // 🔹 appelle ton endpoint d’inscription (à adapter selon ton API)
      await api.post("register/", {
        username,
        email,
        password,
      });

      alert("Compte créé avec succès !");
      navigate("/"); // retourne vers la page de connexion
    } catch (err) {
      console.error(err);
      alert("Erreur lors de l'inscription");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Créer un compte</h2>
      <input
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        placeholder="Nom d'utilisateur"
        required
      />
      <input
        type="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="Adresse email"
        required
      />
      <input
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="Mot de passe"
        required
      />
      <input
        type="password"
        value={password2}
        onChange={(e) => setPassword2(e.target.value)}
        placeholder="Confirme le mot de passe"
        required
      />
      <button type="submit">S'inscrire</button>
    </form>
  );
};

export default Register;
