import React,{useState} from 'react'
import '../Styles/img.css'
import Im from './Img'
const axios = require('axios').default
export default function Reports() {
    
    const generateAVL_En = () =>{
        
        var data = {
            tipo : 0,
            opcion :"Encrypt"
        }
        JSON.stringify(data)
        async function generateAVL(){
            const info = await axios.post('http://localhost:3000/reporte',data )
        }
        generateAVL()

    }
    const generateAVL_DES = () =>{
       
        var data = {
            tipo : 0,
            opcion :"Desencrypt"
        }
        JSON.stringify(data)
        async function generateAVLDES(){
            const info = await axios.post('http://localhost:3000/reporte',data )
        }
        generateAVLDES()

    }
    const generateTablaHash = () =>{
       
        var data = {
            tipo : 6
        }
        JSON.stringify(data)
        async function generateAVLDES(){
            const info = await axios.post('http://localhost:3000/reporte',data )
        }
        generateAVLDES()

    }
    const generateGrafoPensum = () =>{
       
        var data = {
            tipo : 7
        }
        JSON.stringify(data)
        async function generateGrafo(){
            const info = await axios.post('http://localhost:3000/reporte',data )
        }
        generateGrafo()

    }
    
    const MerkleTreeApuntes = () =>{
       
        var data = {
            tipo : 8
        }
        JSON.stringify(data)
        async function generateGrafo(){
            const info = await axios.post('http://localhost:3000/reporte',data )
        }
        generateGrafo()

    }
    const MerkleTreeAsignaciones = () =>{
       
        var data = {
            tipo : 9
        }
        JSON.stringify(data)
        async function generateGrafo(){
            const info = await axios.post('http://localhost:3000/reporte',data )
        }
        generateGrafo()

    }
    const MerkleTreeEstudiantes = () =>{
       
        var data = {
            tipo : 10
        }
        JSON.stringify(data)
        async function generateGrafo(){
            const info = await axios.post('http://localhost:3000/reporte',data )
        }
        generateGrafo()

    }
    return (
        <>
        <div>
            <div class="blue ui buttons">
            <button class="ui button" onClick={generateAVL_En} >AVL Encrypt</button>
            <button class="ui button" onClick={generateAVL_DES}>AVL No Encrypt</button>
            <button class="ui button" onClick ={generateTablaHash}>Table Hash</button>
            </div>
        </div>
        <br/>
        <div>
            <div class="blue ui buttons">
            <button class="ui button" onClick={generateGrafoPensum} >Red</button>
            <button class="ui button" onClick={MerkleTreeApuntes}>Tree Merkle Apuntes</button>
            <button class="ui button" onClick={MerkleTreeAsignaciones}>Tree Merkle Asignaciones</button>
            <button class="ui button" onClick={MerkleTreeEstudiantes}>Tree Merkle Estudiantes</button>
            </div>
        </div>
        </>
    )
}
