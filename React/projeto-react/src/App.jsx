import { useState } from 'react'
import './App.css'
import HelloWorld from './components/HelloWorld'
import SayMyName from './components/SayMyName'
import Pessoa from './components/Pessoa'

function App() {
  const nome = "Cauã"
  const name = "Maria"
  return (
    <div className='App'>
      <h1>Olá React</h1>
      <p>Um site com React feito por {nome}</p>
      <SayMyName nome="Cauã"/>
      <SayMyName nome="Pedro"/>
      <SayMyName nome={name}/>
      <Pessoa 
      nome="Jorge" Idade={35} profissao="Pedreiro" foto="https://imgs.search.brave.com/eWmVS3_Phzb383Ndu034gekv6l6CehKMFPbI6NQqMVs/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTM2/NDE3NjkyMC9wdC9m/b3RvL3dvcmtlci1h/cHBseWluZy10aWxl/LWFkaGVzaXZlLW9u/LXRoZS1mbG9vci5q/cGc_cz02MTJ4NjEy/Jnc9MCZrPTIwJmM9/VnFYUGk2d3hfaTdk/MFdieUhlR2JBbF9y/OGh5UGVSdGFWZEFu/aFRWYzBrRT0"
      />
    </div>
  )
}

export default App
