// Add dark mode

const toggleSwitch = document.querySelector('.nav-link input[type="checkbox"]');
const currentTheme = localStorage.getItem('theme');

if (currentTheme) {
    document.documentElement.setAttribute('data-theme', currentTheme);
  
    if (currentTheme === 'dark') {
        document.getElementById('logo').src  = '/static/logo_jvw_white.svg';
        document.querySelector("link[rel='shortcut icon']").href = "/static/favicon_black.svg";
        toggleSwitch.checked = true;
    }
}

function switchTheme(e) {
    if (e.target.checked) {
        document.documentElement.setAttribute('data-theme', 'dark');
        document.getElementById('logo').src  = '/static/logo_jvw_white.svg';
        localStorage.setItem('theme', 'dark');
    }
    else {        
        document.documentElement.setAttribute('data-theme', 'light');
        document.getElementById('logo').src  = '/static/logo_jvw.svg';
        localStorage.setItem('theme', 'light');
        
    }    
}

toggleSwitch.addEventListener('change', switchTheme, false);



// Add reading time to each blog
var characters = document.getElementById('reading-time');

if(characters)
{
    characters = characters.innerHTML;

    var c = parseInt(characters);
    const avgWordsPerMin = 250;

    setReadingTime();

    function setReadingTime() {
        let count = c / 5;
        let time = Math.ceil(count / avgWordsPerMin);
        document.getElementById("reading-time").innerHTML = time +  " min. read";
    }
}

// Add horizontal scroll indicator only on blog posts

if (characters)
{
    window.onscroll = function() {
        myFunction()
    };
    
    function myFunction() {  
        var winScroll = document.documentElement.scrollTop;  
        var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;  
        var scrolled = (winScroll / height) * 100;  
        document.getElementById("myBar").style.width = scrolled + "%";
    }
}
