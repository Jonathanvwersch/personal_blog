// Add reading time to each blog
var characters = document.getElementById("reading-time").innerHTML;
var c = parseInt(characters)
const avgWordsPerMin = 250;

setReadingTime();

function setReadingTime() {
    let count = c/ 5;
    let time = Math.ceil(count / avgWordsPerMin);
    document.getElementById("reading-time").innerHTML = time +  " min. read";
}