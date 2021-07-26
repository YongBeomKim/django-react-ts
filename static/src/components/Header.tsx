import React from 'react'
import { Link } from 'react-router-dom';
import '../App.css';


export default function Header() {
  return (
    <div className="header">
      <h1>
        <a href="/">React.js</a>
      </h1>
      <div className="menu">
        <a href="/admin" className="link">Django</a>
      </div>
    </div>
  )
}

