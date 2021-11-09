import React,{useState} from 'react'
import { Tab } from 'semantic-ui-react'
import Tabla from './Tabla'
const axios = require('axios').default
export default function ListaApuntes() {
const [notes, setnotes] = useState([])
    var user =localStorage.getItem("user")
    if (user == null || user == undefined){
        return (
            <div>
                No hay usuario logeado       
            </div>
        )

    }else{
        user = JSON.parse(user)
        var data ={
            carnet : user.carnet
        }
        JSON.stringify(data)
        async function fillTable(){
            const lista = await axios.post('http://localhost:3000/listaapuntes',data)
            //console.log(lista.data.Notas)
            setnotes(lista.data.Notas) 
             
             
        }
        fillTable()

        return (
            <Tabla notas = {notes}></Tabla>
        )
    }

    }
    



    
