const loginForm = document.querySelector("#login-form");
const loginInput = document.querySelector("#login-form input");
const greeting = document.querySelector("#greeting");

function onLoginSubmit(event) {
  event.preventDefault();
  const username = loginInput.value;
  loginForm.classList.add("hidden");
  greeting.classList.remove("hidden");
  greeting.innerText = "Hello" + username;
}

function handleLinkClick() {
  console.log("clicked!");
}

loginForm.addEventListener("submit", onLoginSubmit);
