import React from 'react';
import './layout.css';

function Layout({ children }) {
  return (
    <div className="container">
      <header>
        <h1>СпортПлатформа</h1>
      </header>
      <nav>
        {/* Меню уже в App.js */}
      </nav>
      <main>
        {children}
      </main>
      <footer>
        <p>&copy; 2025 SportPlatform</p>
      </footer>
    </div>
  );
}

export default Layout;