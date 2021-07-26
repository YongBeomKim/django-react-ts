import React from "react";
import {render} from "react-dom";
import { BrowserRouter as Router, Route, Switch} from 'react-router-dom';
import './App.css';
import CreateWord from './components/CreateWord';
import Day from './components/Day';
import DayList from './components/DayList';
import Header from './components/Header';
// import PropState from './pages/PropState';


export default function App() { 

  // JSX Template 문법 : 변수 활용이 가능
  // 단 Boolean, Object 의 연산은 불가능
  return (
    <div className="App">

      <Header />
      {/* <PropState age={20} /> */}

      {/* Router 에 따라 화면이 바뀌는 영역 */}
      <Switch>
        <Route exact path="/">
          <DayList />
        </Route>
        <Route path="/day/:day">
          <Day />
        </Route>
        <Route path="/create_word">
          <CreateWord />
        </Route>
      </Switch>

    </div>
  );
}


// Rendering the App.jsx
const appDiv = document.getElementById("root");
render(
  <Router>
    <React.StrictMode>
    <App />
    </React.StrictMode>
  </Router>
, appDiv);