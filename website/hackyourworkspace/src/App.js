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
    <body id="page-top">
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
                  <a class="nav-link js-scroll-trigger" href="#start">
                    Start
                  </a>
                </li>
                <li class="nav-item">
                  <a class="nav-link js-scroll-trigger" href="#stop">
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

        <section id="start" class="bg-light">
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
                    <label>Enter your first name:</label>
                    <br></br>
                    <input id="fname" type="text" />
                    <br></br>

                    <label>Enter your last name:</label>
                    <br></br>
                    <input id="lname" type="text" />
                    <br></br>

                    <label>Enter your phone number:</label>
                    <br></br>
                    <input id="phone" type="text" />
                    <br></br>

                    <p>How long would you like to work today?:</p>
                    <br></br>
                    <div>
                      <label>Hour(s): </label>
                      <input id="hours" type="text" />
                    </div>
                    <div>
                      <label>Minute(s): </label>
                      <input id="minutes" type="text" />
                    </div>
                    <br />
                    <br />

                    <Button
                      style={{ color: "black", background: "grey" }}
                      onClick={() => {
                        start();
                      }}
                    >
                      {" "}
                      Start!
                    </Button>
                  </form>
                </p>
              </div>
            </div>
          </div>
        </section>

        <section id="stop">
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
                  Click the the button below to stop notifications or just text
                  us "STOP".
                  <br></br>
                  <br></br>
                  <Button
                    style={{ color: "black", background: "grey" }}
                    onClick={() => {
                      done();
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
      <footer class="py-5 bg-dark">
        <div class="container">
          <p class="m-0 text-center text-white">Made with ❤ by Team Moments</p>
        </div>
      </footer>
    </body>
  );
}

function done() {
  alert("we'll stop now");
}

function start() {
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "http://3.93.240.100:5000/userupdate", true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.send(
    JSON.stringify({
      num: document.getElementById("phone").value,
      fname: document.getElementById("fname").value,
      lname: document.getElementById("lname").value,
      hours: document.getElementById("hours").value,
      minutes: document.getElementById("minutes").value,
    })
  );
}

export default App;
