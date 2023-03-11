const quotes = [{
        quote: "Without music, life would be a mistake",
        author: "Friedrich Nietzsche",
    },
    {
        quote: "That which does not kill us makes us stronger",
        author: "Friedrich Nietzsche",
    },
    {
        quote: "You must have chaos within you to give birth to a dancing star",
        author: "Friedrich Nietzsche",
    },
    {
        quote: "Sometimes people don't want to hear the truth because they don't want their illusions destoryed",
        author: "Friedrich Nietzsche",
    }
]

const quote = document.querySelector("#quote span:first-child");
const author = document.querySelector("#quote span:last-child");

const currentQuote = quotes[Math.floor(Math.random() * quotes.length)];

quote.innerText = currentQuote.quote;
author.innerText = currentQuote.author;