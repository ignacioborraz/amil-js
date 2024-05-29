document.querySelector("#burguer").addEventListener("click", () => {
  const className = document.querySelector("#opts").className;
  //console.log(className);
  if (className.includes("show")) {
    document.querySelector("#opts").className = "opts hide";
  } else {
    document.querySelector("#opts").className = "opts show";
  }
});
