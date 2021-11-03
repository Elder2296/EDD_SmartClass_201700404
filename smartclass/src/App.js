import React from 'react';
import { BrowserRouter as Router,Route } from 'react-router-dom';
import './App.css';

import Home from './Components/Home'
import Students from './Components/Students'
import admin from './Components/admin';
import './Styles/init.css'
function App() {
  return (
    <>
    <Router>
      
      <div class ="pusher">
        <div class="ui inverted vertical  center aligned segment initial" >
          
          <Route exact path ="/" component ={Home}/>
          <Route exact path ="/Student/" component ={Students}/>
          <Route exact path = "/Admin" component ={admin}/>
             
        </div>

      </div>
    </Router>
    </>
  );
}

export default App;
