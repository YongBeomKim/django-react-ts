import React from 'react';
import { BrowserRouter as Router, Switch, Route} from 'react-router-dom';
import Header from './components/Header';
import Day from './components/Day';
// https://www.npmjs.com/package/typed-css-modules
import styles from './App.css';


const test = process.env.HI

export default function App() {
  return (
    <>
      <Header />
      <Day />
    </>
  )
}