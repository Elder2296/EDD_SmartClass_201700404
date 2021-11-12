import React,{useState} from 'react'
import Asignacion from './Asignacion'


const axios = require('axios').default
export default function Form(props) {
    let arreglo =[]
    const [curso, setcurso] = useState("")
    const [asignar, setasignar] = useState([])
    const [semestre, setsemestre] = useState("")
    const [year, setyear] = useState(2020)
    const view = ()=>{
        
        alert("cursos que lleva: "+asignar)

    }
    const agregar = ()=>{

        
        asignar.push(curso)

        console.log(asignar)

    }
    const Asignar = ()=>{
        alert("pantalones")
        var data = {
            Carnet:"201700404",
            Semestre:semestre,
            Anio:year,
            Cursos: asignar

        }

        JSON.stringify(data)
        
        async function asignacion(){
            const info = await axios.post('http://localhost:3000/Asignar',data)
        }
        
        asignacion()


        var user = localStorage.getItem("user")
        if (user == null || user == undefined){
            

        }else{
            

        }

    }
    return (
        <>

        <div className="ui column centered ">
            <div class="column">
            <div class="ui ">
            <select onChange={e => setcurso(e.target.value)} className = "ui search dropdown">
                <option>Elegir curso</option>
                {
                props.Cursos.map((c,index) =>(
                    <option>{c.curso}</option>
                ))
            }

        </select>
                
             
            </div>
            <br/>
            <div class="ui ">
            <select onChange={e => setsemestre(e.target.value)} className = "ui search dropdown">
                <option>Elegir</option>
                <option>Semestre-1</option>
                <option>Semestre-2</option>
                

            </select>
                
             
            </div>
            <br/>
            <div class="ui ">
            <div class="ui input error">
            <input onChange={e => setyear(e.target.value)} type="number" placeholder="Year..."/>
            </div>
                
             
            </div>
            </div>
            <div class="four column centered row">
            <div class="column">
                <div class="ui blue labels">
                    {
                         
                        
                        arreglo.map((c,index)=>(
                            <a class="ui label">
                                {c}
                            </a>
                        ))
                    }
                </div>
                <br/>
                <br/>
                <button onClick={view} class="positive ui button">Ver Curso</button>
                <button onClick={agregar} class="positive ui button">Agregar</button>
                
                <button onClick={Asignar} class="positive ui button">Asignar</button>
            </div>
            
        </div>
            
        </div>




        
        

        </>
    )
}
