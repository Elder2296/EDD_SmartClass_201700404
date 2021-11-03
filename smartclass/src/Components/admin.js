import React from 'react'
import { BrowserRouter as Router,Route } from 'react-router-dom';
import Nav from './NavAdmin'
import InitAdmin from './InitAdmin';
import Reportes from './Reports';

export default function admin() {
    return (
        <>

        
        
        <Router>
      
            <div class ="pusher">
                <div class="ui inverted vertical  center aligned segment initial" >
                    <Nav/>
                    <Route exact path ="/Admin/" component ={InitAdmin}/>
                    <Route exact path ="/Admin/Reportes" component ={Reportes}/>
                </div>

            </div>
        </Router>
        </>
    )
}
