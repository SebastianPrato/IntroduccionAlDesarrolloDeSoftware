//click barra lateral

const hamburguesa = document.querySelector(".hamburguesa");
const nav = document.querySelector(".nav")

hamburguesa.addEventListener("click", () => {

    const currentWidth = parseInt(window.getComputedStyle(nav).width);

    if (currentWidth === 36) {
        nav.style.width = "255px";
    } else {
        nav.style.width = "36px";
    }
});

//click menu desplegable

let listElements = document.querySelectorAll('.list__button--click');

listElements.forEach(listElement => {
    listElement.addEventListener('click', () => {
        listElement.classList.toggle('arrow')

        let height = 0;
        let menu = listElement.nextElementSibling;
        console.log(menu.scrollHeight)

        if (menu.clientHeight == "0") {
            height = menu.scrollHeight;
        }

        menu.style.height = `${height}px`;
    })
})



const form = document.querySelector('form');
form.addEventListener('submit', (e) => {
  alert("Se ha guardado el mensaje");
  // no llamar a e.preventDefault() para que el formulario se envíe normalmente
});