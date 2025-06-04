import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './styles.css';

import UsersPage from './pages/UsersPage';
import EventsPage from './pages/EventsPage';
import ClubList from './pages/ClubList';
import EquipmentList from './pages/EquipmentList';
import VenueList from './pages/VenueList';
import ScheduleList from './pages/ScheduleList';
import PaymentList from './pages/PaymentList';
import AnalyticsPage from './pages/AnalyticsPage';
import RegistrationList from './pages/RegistrationList';
import ResultList from './pages/ResultList';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';
import HomePage from './pages/HomePage';
import NotFoundPage from './pages/NotFoundPage';
import UserStatus from './components/UserStatus';
import LogoutPage from './pages/LogoutPage';
import UserProfile from './pages/UserProfile'
import StaticPagesList from './pages/StaticPagesList';

function App() {
  return (
    <Router>
      <header className="navbar">
        <h1>Sports Platform</h1>
        <nav>
          <ul className="nav-links">
            <li><Link to="/">Главная</Link></li>
            <li><Link to="/users">Пользователи</Link></li>
            <li><Link to="/events">События</Link></li>
            <li><Link to="/clubs">Клубы</Link></li>
            <li><Link to="/equipment">Инвентарь</Link></li>
            <li><Link to="/venues">Места</Link></li>
            <li><Link to="/schedules">Расписания</Link></li>
            <li><Link to="/payments">Платежи</Link></li>
            <li><Link to="/analytics">Аналитика</Link></li>
            <li><Link to="/registrations">Регистрации</Link></li>
            <li><Link to="/results">Результаты</Link></li>
            <li><Link to="/login">Вход</Link></li>
            <li><Link to="/register">Регистрация</Link></li>
            <li><Link to="/profile">Профиль</Link></li>
            <li><Link to="/info">Информация</Link></li>
          </ul>
        </nav>
        <UserStatus />
      </header>

      <main className="content">
        <Routes>
          <Route path="*" element={<NotFoundPage />} />
          <Route path="/" element={<HomePage />} />
          <Route path="/users" element={<UsersPage />} />
          <Route path="/events" element={<EventsPage />} />
          <Route path="/clubs" element={<ClubList />} />
          <Route path="/equipment" element={<EquipmentList />} />
          <Route path="/venues" element={<VenueList />} />
          <Route path="/schedules" element={<ScheduleList />} />
          <Route path="/payments" element={<PaymentList />} />
          <Route path="/analytics" element={<AnalyticsPage />} />
          <Route path="/registrations" element={<RegistrationList />} />
          <Route path="/results" element={<ResultList />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/register" element={<RegisterPage />} />
          <Route path="/logout" element={<LogoutPage />} />
          <Route path="/profile" element={<UserProfile />} />
          <Route path="/info" element={<StaticPagesList />} />

        </Routes>
      </main>
    </Router>
  );
}

export default App;
