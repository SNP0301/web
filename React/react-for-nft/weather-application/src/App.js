import "./App.css";

function moreInfo() {
  return window.alert("do not come in");
}

function App() {
  return (
    <div className="App">
      <h1 style={{ fontSize: "52px" }}>Welcome to React!</h1>
      <p>Do not give up!</p>
      <img height="400" src="Lion.jpg" alt="what" />
      <br />
      <button onClick={moreInfo}>here is the button!</button>
    </div>
  );
}

export default App; // export default from this file
