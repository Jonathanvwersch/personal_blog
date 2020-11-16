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

// Add blog scrolling effect
window.onscroll = function() {
    myFunction()
};

function myFunction() {  
    var winScroll = document.documentElement.scrollTop;  
    var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;  
    var scrolled = (winScroll / height) * 100;  
    document.getElementById("myBar").style.width = scrolled + "%";
}
