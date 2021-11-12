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
        


        var user = localStorage.getItem("user")
        if (user == null || user == undefined){
            

        }else{
            alert("apunto de asignarse")
            user = JSON.parse(user)
            var data = {
                Carnet:user.carnet,
                Semestre:semestre,
                Anio:year,
                Cursos: asignar

            }

            JSON.stringify(data)
            console.log(data)
            async function asignacion(){
                const info = await axios.post('http://localhost:3000/Asignar',data)
            }
        
            asignacion()

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
            <div class="uid">
            <button onClick={view} class="positive ui button">Ver Curso</button>
                <button onClick={agregar} class="positive ui button">Agregar</button>
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
                
                
                <button onClick={Asignar} class="positive ui button">Asignar</button>
            </div>
            
        </div>
            
        </div>




        
        

        </>
    )
}
