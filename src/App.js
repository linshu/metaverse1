import logo from './logo.svg';
import './App.css';
import "@aws-amplify/ui-react/styles.css";
import { API } from "aws-amplify";

function App() {
  async function fetchItems() {
    const data = await API.get('metaverseapi', '/items')
    console.log(data)
  }

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
