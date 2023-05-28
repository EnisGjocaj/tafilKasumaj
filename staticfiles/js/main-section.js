const aboutContainer = document.getElementById("about-container");
const aboutBtn = document.getElementById("about-btn");
const fieldBtn = document.getElementById("field-btn");
const fieldContainer = document.getElementById("drejtimi-content");
const fieldWrapper = document.getElementById("drejtimi-container");

//lista e drejtimeve

const listOfFields = [

  {
    id: 1,
    title: "Informatikë/Elekronikë",
    imageLink: "Heres the link",
    description: "Drejtimi në Informatikë/Elektronikë ofron nxënësve njohuri dhe aftësi të nevojshme për të projektuar, zhvilluar dhe mirëmbajtur harduer dhe softuer kompjuterik, si dhe pajisje dhe sisteme elektronike. Programi i studimit zakonisht përfshin tema si  algoritmet, hardueri dhe softueri, sistemet operative, elektronika dixhitale, duke i përgatitur studentët për karriera në një gamë të gjerë industriash, duke përfshirë teknologjinë, telekomunikacionin dhe prodhimin.",
    link: "./static/img/informatike.jpg",
  },
  {
    id: 2,
    title: "Mjekësi",
    imageLink: "Heres the link",
    description: "Drejtimi në Mjekësi përgatit nxënësit për karriera në fushën e shëndetësisë dhe mjekësisë, duke ofruar një kuptim të gjerë të anatomisë, fiziologjisë, farmakologjisë dhe praktikave mjekësore.",
    link: "./static/img/mjekësi.jpg",
  },
  {
    id: 3,
    title: "Ekonomi",
    imageLink: "Heres the link",
    description: "Drejtimi në Ekonomi përgatit nxënësit për karriera në financë, konsultim dhe politika publike, duke ofruar një kuptim të gjerë të teorisë ekonomike dhe aplikimeve praktike. Me lëndët në ekonomi studentët zhvillojnë aftësi analitike për një ekonomi globale dinamike.",
    link: "./static/img/ekonomi.jpg",
  },
  {
    id: 4,
    title: "Mekatronikë",
    imageLink: "Heres the link",
    description: "Drejtimi në Mekatronikë përgatit nxënësit për karriera në prodhimin e avancuar, robotikën dhe automatizimin, duke ofruar një kuptim të gjerë të sistemeve mekanike, elektrike dhe kompjuterike.",
    link: "./static/img/mekatronikë.jpg",
  },
  {
    id: 5,
    title: "Mekanikë",
    imageLink: "Heres the link",
    description: "Drejtimi në Mekanikë ofron nxënësve njohuri dhe aftësi të nevojshme për të riparuar dhe mirëmbajtur një gamë të gjerë mjeteve dhe makinave të ndryshme.",
    link: "./static/img/mekanikë.jpg",
  },
  {
    id: 6,
    title: "Ujësjellës",
    imageLink: "Heres the link",
    description: "Drejtimi si Ujësjellës përgatit nxënësit për karriera në industrinë e hidraulikës dhe tubacioneve, duke ofruar një kuptim të hollësishëm të sistemeve hidraulike, furnizimit me ujë, drenazhit dhe heqjes së mbetjeve.",
    link: "./static/img/ujësjellës.jpg",
  },
];

aboutBtn.addEventListener("click", () => {
    const sectionTop = aboutContainer.offsetTop;
    window.scrollTo({
      top:sectionTop,
      behavior: "smooth"
    });
});

fieldBtn.addEventListener("click", () => {
    const sectionTopField = fieldWrapper.offsetTop;
    window.scrollTo({
      top:sectionTopField,
      behavior: "smooth"
    });
});

listOfFields.forEach(course => {

      arrayCourse = [];

     const div = document.createElement("div");

     const newHeader = document.createElement("h4");
     const newText = document.createElement("p");
     const newId = document.createElement("p");
     const newImage = document.createElement("img");

     newHeader.textContent = course.title;
     newText.textContent = course.description;
     newId.innerText = course.id;
     newImage.src = course.link;

     div.setAttribute("id", "div-field");
     newText.setAttribute("id", "newText-field");
     newHeader.setAttribute("id", "newHeader-field");
     newImage.setAttribute("id", "newImage-field");

     div.appendChild(newHeader);
     div.appendChild(newImage);
     div.appendChild(newText);

     fieldContainer.appendChild(div);
     // arrayCourse.push(newHeader.innerText, newText.innerText, newId.innerText, newStatus.innerText)
     // newElement.setAttribute("id", `courseDiv-${course.id}`);
     // newElement.setAttribute("class", "drejtimi-div");
     
     // fieldContainer.appendChild(newElement);
     // const newDiv = document.createTextNode(arrayCourse.join(""));
     // newElement.appendChild(newDiv);
});
