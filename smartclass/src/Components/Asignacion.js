import Form from './Form'
import React,{useState,useEffect} from 'react'

const axios = require('axios').default
export default function Asignacion() {
    const [cursos, setcursos] = useState([])
    const [loading, setloading] = useState(false)
    //var user =localStorage.getItem("user")

    useEffect(()=>{
        async function cargarCursos(){
            const lista = await axios.post('http://localhost:3000/cursos')
            setcursos( lista.data.Cursos)
            setloading(true)
        }
        if (loading ===false){
            cargarCursos()
        }
        
    })
    if (loading === false){
        return (
            <div className="ui segment carga">
                <div className="ui active dimmer ">
                    <div className="ui text loader">

                    </div>

                </div>

            </div>

        )
    }else{
        return (
            <>
            <Form Cursos={cursos} ></Form>
            
            </>
        
        )
    }

    
    
}
