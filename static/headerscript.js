let BarIconBar1 = document.querySelector(".Bar1");
let BarIconBar2 = document.querySelector(".Bar2");
let BarIconBar3 = document.querySelector(".Bar3");
let menuItems = document.querySelector(".menuItems");
let menuOpen = false;

document.querySelector("#BarIcon").addEventListener("click",()=>{
    if (!menuOpen) {
        BarIconBar1.style.transform = "rotate(45deg)";
        BarIconBar3.style.transform = "rotate(-45deg)";
        BarIconBar2.style.opacity = "0";
        menuItems.style.width = "250px";
        menuOpen = true;
    }
    else{
        BarIconBar1.style = "";
        BarIconBar3.style = "";
        BarIconBar2.style = "";
        menuItems.style = "";
        menuOpen = false;
    }
})