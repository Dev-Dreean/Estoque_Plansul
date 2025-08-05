import React, { useState } from 'react';
import Login from './Login';
import Menu from './Menu';
import './App.css';

function App() {
  const [user, setUser] = useState(null);

  return (
    <div className="app-container d-flex justify-content-center align-items-center vh-100 bg-light">
      <div className="access-card shadow-lg rounded">
        <div className="header bg-gradient-primary text-white text-center py-3 px-4 rounded-top">
          <h3 className="mb-0">Acesso</h3>
        </div>
        <div className="body px-4 py-4 bg-white rounded-bottom">
          <div className="fade-in">
            {!user ? (
              <Login onLogin={setUser} />
            ) : (
              <Menu user={user} onLogout={() => setUser(null)} />
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
