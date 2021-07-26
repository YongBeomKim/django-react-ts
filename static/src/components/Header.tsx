import React from 'react'
import { Link } from 'react-router-dom';


export default function Header() {
  return (
    <div className="header">
      <h1>
        <a href="/">Toeic Voca (Test)</a>
      </h1>
      <div className="menu">
        <a href="/create_word" className="link">Add Voc</a>
        <a href="#x" className="link">Add Day</a>
      </div>
    </div>
  )
}

