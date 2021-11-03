import React from 'react'
import '../Styles/TxtArea.css'

export default function listaapuntes() {
    return (
        <>
        <div className="tamanio">
            <table class="ui celled inverted selectable table">
                <thead class=""><tr class=""><th class="">Name</th><th class="">Status</th><th class="">Notes</th></tr>
                </thead>
                <tbody class=""><tr class=""><td class="">John</td><td class="">Approved</td><td class="right aligned">None</td></tr><tr class=""><td class="">Jamie</td><td class="">Approved</td><td class="right aligned">Requires call</td></tr><tr class=""><td class="">Jill</td><td class="">Denied</td><td class="right aligned">None</td></tr>
                </tbody>
            </table>
        </div>
        </>
        )
}
