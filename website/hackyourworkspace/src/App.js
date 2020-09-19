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
	alert(document.getElementById("phone").value)
	var xhr = new XMLHttpRequest();
	xhr.open("POST", "http://3.93.240.100:5000/sms", true);
	xhr.setRequestHeader('Content-Type', 'application/json');
	xhr.send(JSON.stringify({
    		num: document.getElementById("phone").value 
	}));
}

export default App;
