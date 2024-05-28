function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    })
}

document.getElementById('scrollToTopButton').addEventListener('click', scrollToTop)

window.onscroll = function () {
    var button = document.getElementById('scrollToTopButton');

    if (document.body.scrollTop > 40 || document.documentElement.scrollTop > 40) {
        button.style.display = "block"
    } else {
        button.style.display = "none"
    }
};

function fetchearData(texto) {
    fetch("./public/events.json")
        .then((res) => res.json())
        .then((res) => {
            console.log(res);
            if (texto){
                res = res.filter(each => each.artista.toLowerCase().includes(texto.toLowerCase()))
            }
            let events = res
                .map(
                    (each) => `
        <div class="fiesta-item" id="${each.id}">
        <a href="./details.html?id=${each.id}" >
            <img src="${each.imagen}" alt="${each.artista}" height="224px" class="fiesta-item-img">
            <div class="cuadrado"><span class="day">${each.fecha.dia}</span><span class="month">${each.fecha.mes}</span></div>
        </a>
        </div>
        `
                )
                .join("");
            document.querySelector("#events").innerHTML = events;
        })
}

fetchearData()

const input = document.querySelector("#input-search")
input.addEventListener("keyup", () => fetchearData(input.value))