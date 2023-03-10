const h1 = document.getElementById("title");

function handleTitleClick() {
    h1.className = "active";
}

h1.addEventListener("click", handleTitleClick);