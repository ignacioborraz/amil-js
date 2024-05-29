const firstname = document.querySelector("#firstName");
const lastname = document.querySelector("#lastName");
const email = document.querySelector("#email");
const password = document.querySelector("#password");
const birthdate = document.querySelector("#birthdate");
const country = document.querySelector("#country");
const terms = document.querySelector("#terms");

const errorFirstname = document.querySelector("#error-firstname");
const errorLastname = document.querySelector("#error-lastname");
const errorEmail = document.querySelector("#error-email");
const errorPassword = document.querySelector("#error-password");
const errorBirthdate = document.querySelector("#error-birthdate");
const errorCountry = document.querySelector("#error-country");
const errorTerms = document.querySelector("#error-terms");

const formRegister = document.querySelector("#formRegister");

if (firstname && lastname && errorFirstname && formRegister) {
  formRegister.addEventListener("submit", validarFormulario);
} else {
  console.log("error no se puede manejar eventos no encontrados");
}

function validarFormulario(event) {
  event.preventDefault();

  let validation = true;

  if (firstname.value === "") {
    firstname.classList.add("error");
    errorFirstname.textContent = "*Complete con su nombre";
    validation = false;
  } else {
    firstname.classList.remove("error");
    errorFirstname.textContent = "";
  }

  if (lastname.value === "") {
    lastname.classList.add("error");
    errorLastname.textContent = "*Complete con su apellido";
    validation = false;
  } else {
    lastname.classList.remove("error");
    errorLastname.textContent = "";
  }

  if (email.value === "") {
    email.classList.add("error");
    errorEmail.textContent = "*Complete con su email";
    validation = false;
  } else {
    email.classList.remove("error");
    errorEmail.textContent = "";
  }

  if (password.value === "") {
    password.classList.add("error");
    errorPassword.textContent = "*Complete con su contraseña";
    validation = false;
  } else {
    password.classList.remove("error");
    errorPassword.textContent = "";
  }

  if (birthdate.value === "") {
    birthdate.classList.add("error");
    errorBirthdate.textContent = "*Complete con su fecha de nacimiento";
    validation = false;
  } else {
    birthdate.classList.remove("error");
    errorBirthdate.textContent = "";
  }

/*
  if (country.value === "") {
    country.classList.add("error");
    errorCountry.textContent = "*Complete con su país de nacimiento";
    validation = false;
  } else {
    country.classList.remove("error");
    errorCountry.value = "";
  }


  if (terms.value === off) {
    terms.classList.add("error");
    errorTers.textContent = "*Complete con su fecha de nacimiento";
    validation = false;
  } else {
    terms.classList.remove("error");
    errorTerms.value = off;
  }
  */
  if (validation) {
    console.log("Información valida");
  } else {
    console.log("el formulario tienen errores, no se puede enviar");
  }
}
