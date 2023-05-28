const titleInput = document.querySelector('.title-field');
const contentInput = document.querySelector('.form-control-content');
const slugInput = document.querySelector('.slug-field');

const charLimitText = document.getElementById("char-limit");
const addBtn = document.getElementById("button-add");
const contentText = document.querySelector('.form-control-content');

const emailReport = document.querySelector('.email-field');
const textReport  = document.querySelector('.text-field');

const navDevBtn = document.getElementById("box-btn");
const navDevBar = document.getElementById("navbar")

navDevBtn.addEventListener("click", () => {
    navDevBar.classList.toggle("show");
    
});

window.addEventListener("scroll", () => {
    navDevBar.classList.remove("show")
});

titleInput.placeholder = "Titulli";
contentInput.placeholder = "Përmbajtja";
slugInput.placeholder = "Parametri";


contentText.addEventListener('input', function() {
  const currentLength = contentText.value.length;
  const remainingCharacters = 713 - currentLength;

  charLimitText.textContent = `${remainingCharacters} chars left`;
  
  if (remainingCharacters < 20) {
  	charLimitText.style.color = "red";
  }else {
  	charLimitText.style.color = "#94A3B8"
  }
  
  if (currentLength > 713) {
    addBtn.style.display = "none";
  }else {
  	addBtn.style.display = 'block';
  }
});

