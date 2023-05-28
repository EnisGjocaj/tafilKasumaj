const sections = document.querySelectorAll('technology');

const htmlLi = document.getElementById("tech-1");
const cssLi = document.getElementById("tech-2");
const jsLi = document.getElementById("tech-3");
const tailwindLi = document.getElementById("tech-4");
const pythonLi = document.getElementById("tech-5");
const djangoLi = document.getElementById("tech-6");

sections.forEach(section => {
// `#toc a[href="#${section.id}"]`
	const liItem = document.querySelector(`#tech-`); 
})


// Get all the section elements
// const sections = document.querySelectorAll('section');

// // Loop through the sections
// sections.forEach(section => {
//   // Get the corresponding table of contents item
//   const tocItem = document.querySelector(`#toc a[href="#${section.id}"]`);

//   // Create an IntersectionObserver to detect when the section comes into view
//   const observer = new IntersectionObserver(entries => {
//     // If the section is in view, add a "highlight" class to the table of contents item
//     if (entries[0].isIntersecting) {
//       tocItem.classList.add('highlight');
//     } else {
//       // Otherwise, remove the "highlight" class
//       tocItem.classList.remove('highlight');
//     }
//   });

//   // Start observing the section
//   observer.observe(section);
// });
