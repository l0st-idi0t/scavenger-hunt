let clicked = 0;

document.getElementsByTagName('audio')[0].addEventListener('play', (event) => { 
    clicked++;
});

let handle = setInterval(() => {
    if (clicked >= 3) {
        document.getElementById('hint').style.animation = "fadein 2s forwards";
        clearInterval(handle);
    }
}, 500);