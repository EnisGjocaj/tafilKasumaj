const navbar = document.getElementById('navbar-min');
const navBtn = document.getElementById("hamburger-btn-home");


navBtn.addEventListener("click", () => {
    navbar.classList.toggle("show");
});

window.addEventListener("scroll", () => {
    navbar.classList.remove("show")
});