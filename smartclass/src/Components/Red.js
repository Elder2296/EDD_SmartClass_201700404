
import React,{useState} from 'react'

const axios = require('axios').default
export default function Red() {
    const [codigo, setcodigo] = useState("")
    const send = ()=>{
        
        var data = {
            tipo : 5,
            Codigo : codigo
        }
        async function Enviar(){
            const info = await axios.post('http://localhost:3000/reporte',data)
        }
        Enviar()
    }
    return (
        <>
        <div className="ui column centered ">
            <div class="column">
            <h2 class="ui center aligned icon header inverted">
                <i class="circular sitemap icon "></i>
                Red de cursos
            </h2>
            <div class="ui icon input">
                <input type="text" placeholder="ingrese el codigo" onChange={e => setcodigo(e.target.value)}/>
                    <i class="circular search link icon" onClick ={send}></i>
            </div>
            </div>
            <div class="four column centered row">
            <div class="column">
                
            </div>
            
        </div>
            
        </div>
        </>
        
    )
}
