import React from "react";
import "./App.css";
import Emojify from "react-emojione";
import { TextField, Button } from "@material-ui/core";

const options = {
  convertShortnames: true,
  convertUnicode: true,
  convertAscii: true,
  style: {
    backgroundImage: 'url("/path/to/your/emojione.sprites.png")',
    height: 32,
    margin: 4,
  },
  // this click handler will be set on every emoji
  onClick: (event) => alert(event.target.title),
};

function App() {
  return (
    <div className="App">
      <nav
        class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top"
        id="mainNav"
      >
        <div class="container">
          <a class="navbar-brand js-scroll-trigger" href="#page-top">
            HackYourWork{" "}
            <Emojify>
              <span>🧰</span>
            </Emojify>
          </a>
          <button
            class="navbar-toggler"
            type="button"
            data-toggle="collapse"
            data-target="#navbarResponsive"
            aria-controls="navbarResponsive"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarResponsive">
            <ul class="navbar-nav ml-auto">
              <li class="nav-item">
                <a class="nav-link js-scroll-trigger" href="#about">
                  About
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link js-scroll-trigger" href="#services">
                  Start
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link js-scroll-trigger" href="#contact">
                  Stop
                </a>
              </li>
            </ul>
          </div>
        </div>
      </nav>

      <header class="bg-primary text-white" style={{ background: "#4CC3D9" }}>
        <div class="container text-center">
          <h1>
            Start working. Stay Healthy. Be Productive.{" "}
            <Emojify>
              <span>👩‍💻💪🍎</span>
            </Emojify>
          </h1>
          <p class="lead">The notification service built to hold you up.</p>
        </div>
      </header>

      <section id="about">
        <div class="container">
          <div class="row">
            <div class="col-lg-8 mx-auto">
              <h2>About</h2>
              <p class="lead">
                HackYourWork was created with you in mind.{" "}
                <Emojify>
                  <span>💙</span>
                </Emojify>{" "}
                Our goal is to provide you with a service that will keep you
                healthy, productive, and content during and after long work
                hours. Here is a few of the things we offer:{" "}
              </p>
              <ul
                style={{
                  display: "inline-block",
                }}
              >
                <li>Hourly health reminders</li>
                <li>Mental check-ins</li>
                <li>Food and drink suggestions</li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      <section id="services" class="bg-light">
        <div class="container">
          <div class="row">
            <div class="col-lg-8 mx-auto">
              <h2>Start</h2>
              <p class="lead">
                Get started with our super easy setup.
                <Emojify>
                  <span>🤗</span>
                </Emojify>
                <form>
                  <label for="fname">Enter your first name:</label>
                  <br></br>
                  <input type="text" />
                  <br></br>
                  <label for="lname">Enter your last name:</label>
                  <br></br>

                  <input type="text" />
                  <br></br>
                  <label for="phone">Enter your phone number:</label>
                  <br></br>

                  <input type="text" />
                  <br></br>
                  <label for="hours">
                    How many hours would you like to work today?:
                  </label>
                  <br></br>
                  <input type="text" />
                </form>
              </p>
            </div>
          </div>
        </div>
      </section>

      <section id="Done">
        <div class="container">
          <div class="row">
            <div class="col-lg-8 mx-auto">
              <h2>Stop</h2>
              <p class="lead">
                Finished working early?{" "}
                <Emojify>
                  <span>🏁</span>
                </Emojify>{" "}
                Congrats!!!{" "}
                <Emojify>
                  <span>🎉</span>
                </Emojify>
                Click the the button below to stop notifications or just text us
                "STOP".
                <br></br>
                <br></br>
                <Button
                  style={{ color: "black", background: "grey" }}
                  onClick={() => {
                    submit();
                  }}
                >
                  {" "}
                  I'm done!
                </Button>
              </p>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}

/*function App() {
  return (
    <div className="App">
	  <form>
	  	<TextField id="phone" label="phone number" /><br/>
	  	<Button onClick={() => { submit()  }}> Login</Button>
	  </form>
    </div>
  );
}*/

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
