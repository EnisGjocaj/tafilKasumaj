//code below is for the date-time

var dateHeader = document.getElementById("date-header");

var navBtn = document.getElementById("hamburger-btn");
var navBar = document.getElementById("navbar")

navBtn.addEventListener("click", () => {
    navBar.classList.toggle("show");
});

window.addEventListener("scroll", () => {
    navBar.classList.remove("show")
});

var today = new Date();
var year = today.getFullYear();
var month = String(today.getMonth() + 1).padStart(2, '0');
var day = String(today.getDate()).padStart(2, '0');
var fullDate = `${day}-${month}-${year}`;

dateHeader.textContent = `Date: ${fullDate}`;

//code below is to add position fixed to the contents section

var previousScrollY = window.scrollY;

window.addEventListener('scroll', function() {
  const contents = document.getElementById("contents-dev");

    if (window.scrollY < previousScrollY) {
       contents.classList.add("position-absolute");
       contents.classList.remove("position-fixed");
    }else {
        if (isElementInViewport(contents)) {
            contents.classList.remove("position-absolute");
            contents.classList.add('position-fixed');
        } else {
            contents.classList.add('position-absolute');
            contents.classList.remove("position-fixed");
        }
    }

    previousScrollY = window.scrollY;
});

function isElementInViewport(element) {
  const rect = element.getBoundingClientRect();
  return (
    rect.top >= 0 &&
    rect.left >= 0 &&
    rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
    rect.right <= (window.innerWidth || document.documentElement.clientWidth)
  );
}



