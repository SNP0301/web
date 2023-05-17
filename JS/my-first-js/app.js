const fromNumber = document.getElementById("fromNumber");
const fromArithmetic = document.getElementById("fromArithmetic");
const testOutput = document.getElementById("testOutput");
const testForm = document.getElementById("testForm");

function btnClick(event) {
  ///event.preventDefault();
  testForm.classList.add("hidden");
  const testNumber = fromNumber.value;

  testOutput.innerText = `Convert ${testNumber}`;
  alert("hi");
}

testForm.addEventListener("submit", btnClick);
