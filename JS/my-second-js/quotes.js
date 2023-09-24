const quotes = [
  {
    quote: "The way to get started is to quit talking",
    author: "Walt Disney",
  },
  {
    quote: "Keep your innate chaos",
    author: "Niche",
  },
  {
    quote: "No tengo ni idea",
    author: "David",
  },
];

const quote = document.querySelector("#quote span:first-child");
const author = document.querySelector("#quote span:last-child");

console.log(quotes[0]);
author.innerText = quotes[0].author;
