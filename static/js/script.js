// JS for navbar animation on scroll adapted from: https://codepen.io/rauldronca/pen/yQrmeE
var navShape = document.getElementById('main-nav-shape');
var heroShape = document.getElementById('hero-image-shape');
var headerShape = document.getElementsByClassName('head-image-shape')[0];

let currentPos = window.pageYOffset;

var update = () => {
	var newPos = window.pageYOffset;
	var diff = newPos - currentPos;
	let deg = 0;

    if (newPos > 450) {
        deg = 0;
    } else {
        deg = -10;
    }
	
	navShape.style.transform = `skewY(${ deg }deg)`;
    if (heroShape) {
        heroShape.style.transform = `skewY(${ deg }deg)`;
    }
    else if (headerShape) {
        headerShape.style.transform = `skewY(${ deg }deg)`;
    }
	
	currentPos = newPos;
	
	requestAnimationFrame(update);
};

update();