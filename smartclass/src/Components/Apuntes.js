import React,{useState} from 'react'
import { BrowserRouter as Router,Route,Link } from 'react-router-dom';
import Nuevoapunte from './Nuevoapunte';
import listaapuntes from './listaapuntes';
import "../Styles/TxtArea.css"
export default function Apuntes() {
   
    return (
        <Router>
            <div className="ui column centered ">
            <div class="column">
            <div class="ui buttons">
                <Link to={'/Student/Apuntes/nuevo'}><button class="ui button" >Nuevo apunte</button></Link>
                <div class="or"></div>
                <Link to={'/Student/Apuntes/lista'}><button class="ui positive button">Ver apuntes</button></Link>
                </div>
            </div>
            <div class="four column centered row">
            <div class="column">
                <br/>
                <br/>
                <Route exact path="/Student/Apuntes/nuevo" component={Nuevoapunte}/>
                <Route exact path="/Student/Apuntes/lista" component={listaapuntes}/>
            </div>
            
        </div>
            
        </div>
                    
                    
        </Router>
        
    )
}
