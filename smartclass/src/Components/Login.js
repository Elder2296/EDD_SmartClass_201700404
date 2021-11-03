import Nav from './Nav'
import React, { useState } from 'react'
import {useHistory} from 'react-router-dom'
import '../Styles/form.css'
const axios = require('axios').default
export default function Login() {
  let history = useHistory()
    const [carnet, setcarnet] = useState("")
    const [pass, setpass] = useState("")

    const autentication = ()=>{
      var data = {
        CARNET:carnet,
        PASS : pass
      }
      JSON.stringify(data)
      let user = localStorage.getItem("user")
      async function Autentication() {
        //aquí va la comunicacion con la api
        const info = await axios.post('http://localhost:3000/Autentication',data)
        alert(info.data.found+"\n"+info.data.tipo)
        let information = {
          user : info.data.tipo,
          name : info.data.name,
          carnet: info.data.carnet
        }
        if(info.data.tipo ==="Admin"){
          localStorage.setItem("user",JSON.stringify(information))
          history.push('/Admin')
        }else if(info.data.tipo === "Student"){
          localStorage.setItem("user",JSON.stringify(information))
          history.push("/Student/")
        }
      }
      Autentication()
    }
    return (
      <>
      
        <div class="centered ui middle aligned center aligned grid formulario">
  <div class="column">
    <h2 class="ui teal image header">
      
      <div class="content center">
        Log-in 
      </div>
    </h2>
    <form class="ui large form">
      <div class="ui stacked segment">
        <div class="field">
          <div class="ui left icon input">
            <i class="user icon"></i>
            <input type="text" name="email" placeholder="Carnet" onChange ={e => setcarnet(e.target.value)} />
          </div>
        </div>
        <div class="field">
          <div class="ui left icon input">
            <i class="lock icon"></i>
            <input type="password" name="password" placeholder="Password" onChange ={e => setpass(e.target.value)}  />
          </div>
        </div>
        <div class="ui fluid large teal submit button" onClick = {autentication}> Ingresar</div>  
      </div>

      

    </form>

    
  </div>
</div>
</>
    )
}
