// Input Fields
const name = document.getElementById("name");
const birthday = document.getElementById("birthday");
const nic = document.getElementById("nic");
const address = document.getElementById("address");
const telephone = document.getElementById("telephone");
const zscore = document.getElementById("zscore");

// form
const form = document.getElementById("form");

// validators for personal information

function validateName() {
  // check if empty
  if (checkIfEmpty(name)) return;

  //   check if it has only letters
  if (!checkIfOnlyLetters(name)) return;
  return true;
}

function validateGender() {
  // check if atleast one option is selected
  let radios = document.getElementsByName("gender");
  let formValid = false;
  for (let i = 0; i < radios.length; i++) {
    if (radios[i].checked == true) {
      formValid = true;
      break;
    }
  }
  const gender = document.getElementById("male");
  if (formValid == true) {
    setValid(gender);
    return true;
  } else {
    setInvalid(gender, `${gender.name} must be selected.`);
    return false;
  }
}

function validateNIC() {
  // check if empty
  if (checkIfEmpty(nic)) return;

  // check if has only numbers
  if (!checkIfOnlyNumbers(nic)) return;
  return true;
}

function validateAddress() {
  // check if empty
  if (checkIfEmpty(address)) return;

  return true;
}

function validateTelephone() {
  // check if empty
  if (checkIfEmpty(telephone)) return;

  // check if has only numbers
  if (!checkIfOnlyNumbers(telephone)) return;

  //   check if has only 10 digits
  if (checkIfMeetLength(telephone, 10)) return;
  return true;
}

function validateZscore() {
  // check if empty
  if (checkIfEmpty(zscore)) return;

  // check if has only numbers
  if (!checkIfOnlyNumbers(zscore)) return;
  return true;
}

// validators for course information

function validateCourseSelection() {
  // check if atleast one option is selected
  let radios = document.getElementsByName("combination");
  let formValid = false;
  for (let i = 0; i < radios.length; i++) {
    if (radios[i].checked == true) {
      formValid = true;
      break;
    }
  }
  const combination = document.getElementById("sor");
  if (formValid == true) {
    setValid(combination);
    return true;
  } else {
    setInvalid(combination, `${combination.name} must be selected.`);
    return false;
  }
}

function validateCombinationSelector(){

  
}

// utility Functions

function checkIfEmpty(field) {
  if (isEmpty(field.value.trim())) {
    // set field invalid
    setInvalid(field, `${field.name} must not be empty.`);
    return true;
  } else {
    // set field valid
    setValid(field);
    return false;
  }
}

function isEmpty(value) {
  if (value === "") {
    return true;
  } else {
    return false;
  }
}

function setInvalid(field, message) {
  const formControl = field.parentElement;

  //   add error message inside the span tag
  const span = formControl.querySelector("span");

  span.innerHTML = message;

  //    add the error class
  formControl.className = "form-control error";
}

function setValid(field) {
  const formControl = field.parentElement;
  //    add the success class
  formControl.className = "form-control success";
}

function checkIfOnlyLetters(field) {
  if (/^[a-zA-Z ]+$/.test(field.value)) {
    setValid(field);
    return true;
  } else {
    setInvalid(field, `${field.name} must contain only letters `);
    return false;
  }
}

function checkIfOnlyNumbers(field) {
  if (/^[0-9 ]+$/.test(field.value)) {
    setValid(field);
    return true;
  } else {
    setInvalid(field, `${field.name} must contain only numbers`);
    return false;
  }
}

function checkIfMeetLength(field, maxLength) {
  if (field.value.length <= maxLength) {
    setValid(field);
    return true;
  } else {
    setInvalid(field, `${field.name} must contain only 10 digits`);
    return false;
  }
}
