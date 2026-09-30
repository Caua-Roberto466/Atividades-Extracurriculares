import { useState } from 'react'
import './App.css'
import HelloWorld from './components/HelloWorld'
import SayMyName from './components/SayMyName'
import Pessoa from './components/Pessoa'
import Frase from './components/Frase'

function App() {
  const nome = "Cauã"
  const name = "Maria"
  return (
    <div className='App'>
      <h1>Olá React</h1>
      <p>Um site com React feito por {nome}</p>
      <Frase/>
      
    </div>
  )
}

export default App
