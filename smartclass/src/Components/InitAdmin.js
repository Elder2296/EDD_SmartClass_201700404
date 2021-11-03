import React from 'react'
import { BrowserRouter as Router,Route,Link } from 'react-router-dom';
import Load from './Load';
export default function InitAdmin() {
    return (
        <Router>
            <div className="ui column centered ">
            <div class="column">
            <div class="ui buttons">
                <Link to={'/Admin/Load'}><button class="ui button" >Load Students</button></Link>
                <div class="or"></div>
                <Link to={'/Admin/Reportes'}><button class="ui positive button">Load pensum</button></Link>
                </div>
            </div>
            <div class="four column centered row">
            <div class="column">
                <br/>
                <br/>
                <Route exact path="/Admin/Load'" component={Load}/>
                
            </div>
            
        </div>
            
        </div>
                    
                    
        </Router>
    )
}
