function scrollToTop(){
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    })
}

document.getElementById('scrollToTopButton').addEventListener('click', scrollToTop)

window.onscroll = function () {
    var button = document.getElementById('scrollToTopButton');

    if(document.body.scrollTop > 40 || document.documentElement.scrollTop > 40){
        button.style.display = "block"
    }else{
        button.style.display = "none" 
    }
};