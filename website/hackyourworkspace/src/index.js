import React, { Component } from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import * as serviceWorker from "./serviceWorker";
import "./assests/css/bootstrap.min.css";
import "./assests/css/scrolling-nav.css";

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById("root")
);

/*const Emoji = (props) => (
  <span
    className="emoji"
    role="img"
    aria-label={props.label ? props.label : ""}
    aria-hidden={props.label ? "false" : "true"}
  >
    {props.symbol}
  </span>
);

class ReactComponent extends Component {
  render() {
    return (
      <div>
        <h1>
          How to use <Emoji symbol="✨" />
          emojis
          <Emoji symbol="✨" /> in React
        </h1>
        <h3>Copy & paste: 🐑</h3>
        <p>Bad - it renders but throws an ESLint error (check the console)</p>
        <h3>Unicode escape: {"\u1F411"}</h3>
        <p>
          Bad - it works for some emojis (<i>e.g.</i> {"\u2728"}) but will not
          render our sheep
        </p>
        <h3>
          Using <code>span</code>:{" "}
          <span role="img" aria-label="sheep">
            🐑
          </span>
        </h3>
        <p>Better - but a little verbose</p>
        <h3>
          Component: <Emoji label="sheep" symbol="🐑" />
        </h3>
        <p>
          Best - easily reuseable with an <code>aria-label</code> (above), or
          without: <Emoji symbol="🐑" />
        </p>
      </div>
    );
  }
}
*/
//ReactDOM.render(<ReactComponent />, document.getElementById("root"));
// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
