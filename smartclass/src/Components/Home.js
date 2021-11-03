import React from 'react'
import '../Styles/Home.css'
import { BrowserRouter as Router,Route } from 'react-router-dom'

import Login from './Login';
import Register from './Register';
import Init from './Init';
import Navbar from './Nav'
export default function Home() {
    return (
        <>
        
        <Router>
      
            
                <Navbar/>
                <Route exact path ="/" component ={Init}/>     
                <Route exact path ="/Login" component ={Login}/>
                <Route exact path ="/Register" component ={Register}/>
                   
                
        </Router>
        
        </>
    )
}
