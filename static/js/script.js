// JS for navbar animation on scroll adapted from: https://codepen.io/rauldronca/pen/yQrmeE
const navShape = document.getElementById('main-nav-shape');
const heroShape = document.getElementById('hero-image-shape');
const headerShape = document.getElementsByClassName('head-image-shape')[0];

let currentPos = window.pageYOffset;

const update = () => {
	const newPos = window.pageYOffset;
	const diff = newPos - currentPos;
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
}

update();