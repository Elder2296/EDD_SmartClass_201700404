import React from 'react'
import Nav from './NavStudents'
import { BrowserRouter as Router,Route } from 'react-router-dom';
import Inicio from './InitStudents'
import Apuntes from './Apuntes';
import Red from './Red';
import Tareas from './Tareas';
import Asignacion from './Asignacion';
import ReportAsignacion from './ReportAsignacion';
export default function Students() {
    return (
        <>

        
        
        <Router>
      
            <div class ="pusher">
                <div class="ui inverted vertical  center aligned segment initial" >
                    <Nav/>
                    <Route exact path ="/Student/" component ={Inicio}/>
                    <Route exact path ="/Student/Apuntes" component ={Apuntes}/>
                    <Route exact path ="/Student/Tareas" component ={Tareas}/>
                    <Route exact path ="/Student/Red" component ={Red}/>
                    <Route exact path ="/Student/Asignacion" component ={Asignacion}/>
                    <Route exact path ="/Student/ReporteAsignacion" component ={ReportAsignacion}/>
                    
                </div>

            </div>
        </Router>
        </>
        
    )
}
