// Add horizontal scroll indicator on blog posts
window.onscroll = function() {
    myFunction()
};

function myFunction() {  
    var winScroll = document.documentElement.scrollTop;  
    var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;  
    var scrolled = (winScroll / height) * 100;  
    document.getElementById("myBar").style.width = scrolled + "%";
}

// Add dark mode

const toggleSwitch = document.querySelector('.nav-link input[type="checkbox"]');
const currentTheme = localStorage.getItem('theme');

if (currentTheme) {
    document.documentElement.setAttribute('data-theme', currentTheme);
  
    if (currentTheme === 'dark') {
        if (document.getElementById('logo').src) {
            document.getElementById('logo').src  = '/static/logo_jvw_white.svg';
        } 

        if ( document.getElementById('profile').srcsrc) {
            document.getElementById('profile').src  = '/static/profile_black.png';
        } 
        
        document.querySelector("link[rel='shortcut icon']").href = "/static/favicon_black.svg";
        toggleSwitch.checked = true;
    }
}

function switchTheme(e) {
    if (e.target.checked) {
        document.documentElement.setAttribute('data-theme', 'dark');
        if (document.getElementById('logo').src) {
            document.getElementById('logo').src  = '/static/logo_jvw_white.svg';
        } 

        if ( document.getElementById('profile').srcsrc) {
            document.getElementById('profile').src  = '/static/profile_black.png';
        } 
        
        localStorage.setItem('theme', 'dark');
    }
    else {        
        document.documentElement.setAttribute('data-theme', 'light');
        if (document.getElementById('logo').src) {
            document.getElementById('logo').src = '/static/logo_jvw.svg';
        }  

        if (document.getElementById('profile').src) {
            document.getElementById('profile').src  = '/static/profile.png';
        } 
        
        localStorage.setItem('theme', 'light');
        
    }    
}

toggleSwitch.addEventListener('change', switchTheme, false);



// Add reading time to each blog
var characters = document.getElementById("reading-time").innerHTML;
var c = parseInt(characters);
const avgWordsPerMin = 250;

setReadingTime();

function setReadingTime() {
    let count = c / 5;
    let time = Math.ceil(count / avgWordsPerMin);
    document.getElementById("reading-time").innerHTML = time +  " min. read";
}
