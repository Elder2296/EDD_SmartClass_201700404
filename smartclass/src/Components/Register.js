import { jsxOpeningElement } from '@babel/types'
import React, { useState } from 'react'
import Nav from './Nav'
import '../Styles/form.css'

const axios = require('axios').default

export default function Register() {
    const [carnet, setscarnet] = useState(1)
    const [dpi, setdpi] = useState("")
    const [name, setname] = useState("")
    const [carrera, setcarrera] = useState("")
    const [email, setemail] = useState("prueba@gmail.com")
    const [creditos, setcreditos] = useState(0)
    const [age, setage] = useState(0)
    const [pass, setpass] = useState("")

    const send =()=>{
        console.log("carnet: "+carnet+" contraseña:"+pass+" email: "+email)
        var data ={
            carnet:carnet,
            DPI:dpi,
            nombre: name,
            carrera: carrera,
            correo: email,
            password: pass,
            creditos: creditos,
            edad: age,

        }
        JSON.stringify(data)
        async function  addUser() {
            const info = await axios.post('http://localhost:3000/estudiante', data)
            alert(info.data.message)
            
        }
        addUser()
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
                                    <input type="text" name="carnet" placeholder="Carnet" onChange={e => setscarnet(e.target.value)} />
                            </div>
                        </div>
                        <div class="field">
                            <div class="ui left icon input">
                                <i class="user icon"></i>
                                    <input type="text" name="Dpi" placeholder="Dpi" onChange={e => setdpi(e.target.value)}  />
                            </div>
                        </div>
                        <div class="field">
                            <div class="ui left icon input">
                                <i class="user icon"></i>
                                    <input type="text" name="name" placeholder="Name"  onChange={e => setname(e.target.value)}/>
                            </div>
                        </div>
                        <div class="field">
                            <div class="ui left icon input">
                                <i class="user icon"></i>
                                    <input type="text" name="Carrera" placeholder="Carrera" onChange={e => setcarrera(e.target.value)} />
                            </div>
                        </div>
                        <div class="field">
                            <div class="ui left icon input">
                                <i class="user icon"></i>
                                    <input type="email" name="email" placeholder="user@domine.com" onChange={e => setemail(e.target.value)} />
                            </div>
                        </div>
                        <div class="field">
                            <div class="ui left icon input">
                                <i class="user icon"></i>
                                    <input type="text" name="credits" placeholder="creditos" onChange={e => setcreditos(e.target.value)} />
                            </div>
                        </div>
                        <div class="field">
                            <div class="ui left icon input">
                                <i class="user icon"></i>
                                    <input type="text" name="edad" placeholder="edad"  onChange={e => setage(e.target.value)} />
                            </div>
                        </div>
                        <div class="field">
                            <div class="ui left icon input">
                                <i class="lock icon"></i>
                                    <input type="password" name="password" placeholder="Password" onChange={e => setage(e.target.value)}  />
                            </div>
                        </div>
                        <div class="ui fluid large teal submit button " onClick ={send}> Ingresar</div>  
                    </div>

      

                </form>

    
            </div>
        </div>
        </>
    )
}
