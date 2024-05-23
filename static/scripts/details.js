const query = location.search;
const params = new URLSearchParams(query);
const id = params.get("id");
//console.log(id);

fetch("/public/events.json")
  .then((res) => res.json())
  .then((res) => {
    //console.log(res);
    const one = res.find((each) => each.id === Number(id));
    console.log(one);
    /* document.querySelector("#details").innerHTML = `
    
    ` */
  });
