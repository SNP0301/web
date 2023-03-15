import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
/// import "./styles.css"; /// CSS는 Proptypes와 다르게 모든 component의 색을 바꾸기 때문에 좋지 않다.

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);
