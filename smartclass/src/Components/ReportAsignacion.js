import React,{useState} from 'react'

const axios = require('axios').default
export default function ReportAsignacion() {
    const [anio, setanio] = useState(2020)
    const [semestre, setsemestre] = useState(1)

    const enviar= () => {

        var user = localStorage.getItem("user")
        if (user == null || user == undefined){
            

        }else{
            user = JSON.parse(user)
            var data ={
                tipo:4,
                carnet:user.carnet,
                año: anio,
                semestre: semestre
            }
            JSON.stringify(data)
            async function Report(){
                const info = await axios.post('http://localhost:3000/reporte',data)
            }
            Report()

        }




        
    }

    return (
        <>
        <div className="ui column centered ">
            <div class="column">
            <div class="ui ">
               
            <div class="ui input error">
                <input onChange={e => setanio(e.target.value)} type="number" placeholder="Año..."/>
            </div>
            <br/>
            <br/>
            <div class="ui input error">
                <input onChange={e => setsemestre(e.target.value)} type="number" placeholder="Semestre..."/>
            </div>
            <br/>
            <br/>
            <div class="ui input error">
            <button onClick={enviar} class="positive ui button">Generar Reporte</button>
            </div>
                </div>
            </div>
            <div class="four column centered row">
            <div class="column">
                <br/>
                <br/>
                
                
            </div>
            
        </div>
            
        </div>
        </>
    )
}
