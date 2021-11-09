import React from 'react'

export default function Fila(props) {
    return (
        <tr>
        <td>{props.numero}</td>
        <td>{props.titulo}</td>
        <td>{props.contenido}</td>
        
        
    </tr>
    )
}
