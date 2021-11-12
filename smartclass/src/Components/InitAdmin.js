import React,{useState} from 'react'

import Load from './Load';
import '../Styles/TxtArea.css'

const axios = require('axios').default
export default function InitAdmin() {
    const [content, setcontent] = useState("")
    const loadStudents= ()=>{
        var data = JSON.parse(content)
        async function loadStudents(){
            const info = await axios.post('http://localhost:3000/estudiantes',data)
        }
        loadStudents()
        
    }
    const loadPensum= ()=>{
        var data = JSON.parse(content)
        async function loadPensum(){
            const info = await axios.post('http://localhost:3000/cursosPensum',data)
        }
        loadPensum()
        
    }
    const loadApuntes= ()=>{
        var data = JSON.parse(content)
        async function loadApuntes(){
            const info = await axios.post('http://localhost:3000/cargarapuntes',data)
        }
        loadApuntes()
        
    }
    return (
        
            <div className="ui column centered ">
            <div class="column">
            <div class="ui buttons">
                <button class="ui button" onClick={loadStudents} >Load Students</button>
                <div class="or"></div>
                <button class="ui positive button"  onClick={loadPensum}>Load pensum</button>
            </div>
                <br/>
                <br/>
            <div class="ui buttons">
                
                <button class="ui positive button"  onClick={loadApuntes}>Load Apuntes</button>
            </div>
            </div>
            
            <div class="four column centered row">
            <form class="ui form">
        
                <br/>
                <div>
                    <textarea placeholder="Ingresa el JSON" className="tamanio" onChange={e=>setcontent(e.target.value)}>
                </textarea>
                </div>
                
            </form>
            
        </div>
            
        </div>
                    
                    
        
    )
}
