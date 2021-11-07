import React, { Component } from 'react';
import '../Styles/img.css';

import tabla from '../images/tablaHash.png'
class App extends Component {
  render() {
    return (
      <div className="dimensiones">
        {/*Aqui utilizamos la url donde esta alojada la imagen*/}
        <img src="/home/losa/Escritorio/Reportes_F3/avl.png" />
      </div>
    );
  }
}

export default App;