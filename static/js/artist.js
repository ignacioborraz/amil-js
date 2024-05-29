const query = location.search;
const params = new URLSearchParams(query);
const id = params.get("id");
//console.log(id);

fetch("./public/artists.json")
  .then((res) => res.json())
  .then((res) => {
    //console.log(res);
    const one = res.find((each) => each.id === Number(id));
    //console.log(one);
    document.querySelector("#main").innerHTML = `
    <img class="w-full h-400 fit my-30 break-pt-30 break-pb-30 grayscale"
      src="${one.foto}" alt="${one.artista}">
    <article
      class="static break-absolute abs-left break-ml-30 break-pb-30 p-10 bg-primary flex column j-between a-center break-a-start">
      <p class="titles size-40">${one.artista}</p>
    </article>
    <article
      class="static break-absolute abs-rigth break-mr-30 break-pt-30 p-10 bg-primary flex column j-between a-center break-a-end">
      ${one.genero
        .map((each) => `<p class="titles size-0">${each}</p>`)
        .join("")}
    </article>
    `;
    document.querySelector("#details").innerHTML = `<p>${one.descripcion}</p>`;
    document.querySelector("#video").innerHTML = one.video;
  });
