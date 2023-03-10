const loginForm = document.querySelector("#login-form");
const loginButton = document.getElementById("box");
const greeting = document.querySelector("#greeting");
const USERNAME_KEY = "username";

function btnClick(event) {
    event.preventDefault();

    loginForm.classList.add("hidden");
    const username = loginButton.value;
    localStorage.setItem("USERNAME_KEY", username);
    greeting.innerText = `Hello ${username}`;
    greeting.classList.remove("hidden");
    paintGreetings(username);
}

function paintGreetings(username) {
    greeting.innerText = `Again, ${username}`;
    greeting.classList.remove("hidden");
}

loginForm.addEventListener("submit", btnClick);

const savedUsername = localStorage.getItem("USERNAME_KEY");

if (savedUsername == null) {
    loginForm.classList.remove("hidden");
    loginForm.addEventListener("submit", btnClick);
} else {
    paintGreetings(savedUsername);
}