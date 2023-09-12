const loginInput = document.querySelector("#login-form input");
const loginButton = document.querySelector("#login-form button");

function onLoginBtnClick() {
  console.log("button!!!!!", loginInput.value, "entered");
}

loginButton.addEventListener("click", onLoginBtnClick);
