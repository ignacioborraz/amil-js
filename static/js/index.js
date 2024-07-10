function scrollToTop() {
  window.scrollTo({
    top: 0,
    behavior: "smooth",
  });
}

document
  .getElementById("scrollToTopButton")
  .addEventListener("click", scrollToTop);

window.onscroll = function () {
  var button = document.getElementById("scrollToTopButton");

  if (document.body.scrollTop > 40 || document.documentElement.scrollTop > 40) {
    button.style.display = "block";
  } else {
    button.style.display = "none";
  }
};

function fetchearData(texto) {
  fetch("http://127.0.0.1:5000/api/eventos")
    .then((res) => {
      if (!res.ok) {
        throw new Error('Network response was not ok ' + res.statusText);
      }
      return res.json();
    })
    .then((res) => {
      console.log(res);
      if (texto) {
        res = res.filter((each) =>
          each.artista.nombre.toLowerCase().includes(texto.toLowerCase())
        );
      }
      let events = res
        .map(
          (each) => `
        <div class="fiesta-item" id="${each.id}">
        <a href="./details.html?id=${each.id}" >
            <img src="${each.artista.imagen}" alt="${each.artista.nombre}" height="224px" class="fiesta-item-img">
            <div class="cuadrado"><span class="day">${each.dia}</span><span class="month">${each.mes}</span></div>
            <div class="rectangulo"><span class="day">${each.artista.nombre}</span></div>
        </a>
        </div>
        `
        )
        .join("");
      document.querySelector("#events").innerHTML = events;
    })
    .catch((error) => {
      console.error('Error fetching data:', error);
    });
}

fetchearData();

const input = document.querySelector("#input-search");
input.addEventListener("keyup", () => fetchearData(input.value));

// fetch("./public/artists.json")
//   .then((res) => res.json())
//   .then((res) => {
//     let artists = res
//       .sort((a, b) => a.artista.localeCompare(b.artista))
//       .map(
//         (each) => `
//           <a href="./artist.html?id=${each.id}" class="fiesta-item-v2">
//             <div class="wrapper">
//                 <img src="${each.avatar}" alt="${each.artista}" class="fiesta-item-img-v2">
//             </div>
//             <div class="fiesta-item-detail-v2">
//                 <p class="fiesta-item-detail-title-v2">${each.artista}</p>
//                 <p class="fiesta-item-detail-subtitle-v2">DJ ${each.nacionalidad}</p>
//                 <p class="fiesta-item-detail-subtitle-v2">${each.genero[0]}</p>
//             </div>
//           </a>`
//       )
//       .join("");
//     document.querySelector("#top").innerHTML = artists;
//   });