let abstract = document.querySelector(".abstract")
let aboutAuthor = document.querySelector(".aboutAuthor")
let abstractText = document.querySelector(".abstractText")
let authorText = document.querySelector(".authorText")

function showBook() {
    abstract.style = "background : #a3282b;color : white";
    aboutAuthor.style = "background : white;color : black";

    abstractText.style = "display : block;"
    authorText.style = "display : none;"
}

function showAuthor() {
    aboutAuthor.style = "background : #a3282b;color : white";
    abstract.style = "background : white;color : black";

    authorText.style = "display : block;"
    abstractText.style = "display : none;"
}