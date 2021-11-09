import React from 'react'
import Fila from './Fila'
export default function Tabla(props) {
    let contador= 0
    console.log("lo que lleva el props en la tabla")
    console.log(props)
    return (
        <>
        <table className="ui inverted teal table">
            <thead>
                <tr>
                    <th>No</th>
                    <th>titulo</th>
                    <th>Contenido</th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
            {
                props.notas.map((c,index)=>(
                    
                    <Fila 
                        numero={contador =contador+1}
                        titulo={c.titulo}
                        contenido={c.contenido}
                        
                        
                    />
                    
                )
                
                )
            }

                
            </tbody>

        </table>
        
        </>
    )
}
