const query = location.search;
const params = new URLSearchParams(query);
const id = params.get("id");
console.log(id);

fetch("./public/events.json")
  .then((res) => res.json())
  .then((res) => {
    //console.log(res);
    const one = res.find((each) => each.id === Number(id));
    console.log(one);
    document.querySelector("#main").innerHTML = `
    <img class="w-full h-400 fit my-30 break-pt-30 break-pb-30 grayscale"
      src="${one.imagen}" alt="${one.artista}">
    <article
      class="static break-absolute abs-left break-ml-30 break-pb-30 p-10 bg-primary flex column j-between a-center break-a-start">
      <p class="titles size-40">${one.artista}</p>
    </article>
    <article
      class="static break-absolute abs-rigth break-mr-30 break-pt-30 p-10 bg-primary flex column j-between a-center break-a-end">
      <p class="titles size-30">${one.lugar}</p>
      <p class="titles size-20">${one.fecha.dia} de ${one.fecha.mes} de ${one.fecha.año}</p>
    </article>
    `;
    let tickets = one.entradas
      .map(
        (each) => `
          <article class="bg-secondary p-15 m-10 w-400 round flex column j-between">
            <p class="buttons size-20 round">${each.tipo.toUpperCase()} TICKET - $${
          each.precio
        }</p>
            <p class="buttons size-16 round">Disponibles: 20.000</p>
            <button class="bg-primary hover-bg-black size-16 p-10 mt-10 buttons round cursor">Comprar!</button>
          </article>
        `
      )
      .join("");
    document.querySelector("#tickets").innerHTML = tickets;
    let lineup = one.lineup
      .map(
        (each) => `
        <article class="bg-white p-10 m-10 w-400 round">
          <img class="w-full h-400 round fit"
            src="${each.avatar}"
            alt="kevin" />
          <p class="titles primary size-30 center">${each.artista}</p>
          <p class="primary size-20 center">${each.desde} hasta las ${each.hasta}</p>
        </article>
      `
      )
      .join("");
    document.querySelector("#lineup").innerHTML = lineup;
  });
