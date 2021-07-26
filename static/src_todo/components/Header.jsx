import React from 'react';
import { Link } from 'react-router-dom';

export default function Header() {
  return (
    <div className="header">
      <h1>
        <Link to="/">Toeic Voca(Super)</Link>
      </h1>
      <div className="menu">
        <Link to="/create_word" className="link">Add Voca</Link>
        <a href="#x" className="link">Add Day</a>
      </div>
    </div>
  )
}
