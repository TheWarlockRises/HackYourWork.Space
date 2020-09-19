import React from 'react';
import './App.css';
import { TextField, Button } from '@material-ui/core';

function App() {
  return (
    <div className="App">
	  <form>
	  	<TextField id="phone" label="phone number" /><br/>
	  	<Button onClick={() => { submit()  }}> Login</Button>
	  </form>
    </div>
  );
}

function submit() {
	alert()
}

export default App;
