// JS for navbar animation on scroll adapted from: https://codepen.io/rauldronca/pen/yQrmeE
const navShape = document.getElementById('main-nav-shape');
const imgShape = document.getElementById('hero-image-shape');

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
    if (imgShape) {
        imgShape.style.transform = `skewY(${ deg }deg)`;
    }
	
	currentPos = newPos;
	
	requestAnimationFrame(update);
}

update();