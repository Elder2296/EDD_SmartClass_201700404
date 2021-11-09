import React,{useState} from 'react'

import '../Styles/TxtArea.css'

const axios = require('axios').default

export default function Nuevoapunte() {
    const [titulo, settitulo] = useState("")
    const [content, setcontent] = useState("")
    let [user, setuser] = useState("None")
    let [carnet, setcarnet] = useState(0)
    var data = localStorage.getItem('user')
    if(data ==null || data == undefined){
        user = 'Null'

    }else{
        data = JSON.parse(data)
        if(data.user ==='Student'){
            user = data.name
            carnet = data.carnet
        }
    }
    const send = () =>{
        var data = {
            CARNET : carnet,
            TITULO : titulo,
            CONTENIDO : content

        }
        JSON.stringify(data)
        async function sendNote(){
            const info = await axios.post('http://localhost:3000/Apuntes',data)
        }
        sendNote()
    }

    return (
        <>
        <div class="ui label">
        <i class="big user icon"></i> {user}
        </div>
        <div class="ui label">
        <i class="big id card icon"></i> {carnet}
        </div>
            
        <br/>
        <br/>
    <form class="ui form">
        <div>
        <input className="tamanio" type="text" name="titulo" placeholder="Titulo" onChange={e=> settitulo(e.target.value)}/>
        
        </div>
        <br/>
        <div>
            <textarea placeholder="Escribe tu apunte" className="tamanio" onChange={e=>setcontent(e.target.value)}>
        </textarea>
        </div>
        
    </form>
    <div>
        <br/>
    <button class="blue ui  button" onClick={send}>Guardar</button>
    </div>
        </>
    )
}
