let carousel = document.querySelector(".carousel");
let carouselContainer = document.querySelector(".carouselContainer")
let scroll = 0;
let previousCard = carousel.children[0];
let currIndex = 1;
let bgColor = ["pink","yellow","orange","aquamarine","cornflowerblue","tomato","teal","skyblue"]

function scrolltoleft() {
    if (currIndex == 1) {
        currIndex = 12;
        carousel.style.scrollBehavior = "unset"
        carousel.scrollLeft = currIndex * (window.innerWidth / 2);
        carousel.style.scrollBehavior = "";
    }
    currIndex--;
    console.log(currIndex);
    carousel.scrollLeft = currIndex * (window.innerWidth / 2);
    carouselContainer.style.background = bgColor[currIndex % bgColor.length];
}
function scrolltoright() {
    if (currIndex == 31) {
        currIndex = 20;
        carousel.style.scrollBehavior = "unset"
        carousel.scrollLeft = currIndex * (window.innerWidth / 2);
        carousel.style.scrollBehavior = "";
    }
    currIndex++;
    carousel.scrollLeft = currIndex * (window.innerWidth / 2);

    console.log(currIndex);
    carousel.style = "";
    carouselContainer.style.background = bgColor[currIndex % bgColor.length];
}

carousel.scrollLeft = 0;
carousel.scrollLeft += (window.innerWidth / 2);