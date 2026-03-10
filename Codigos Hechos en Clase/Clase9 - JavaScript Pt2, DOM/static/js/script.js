//Consulta que nos devuelve por consola el contenido del segundo parrafo
const parrafos = document.getElementsByTagName("p")
const textoParrafo2 = parrafos[1].innerText
console.log(textoParrafo2)

//Boton de alerta que nos da un alert cada vez que clickeamos en él
const botonAlerta = document.getElementById("alerta")

botonAlerta.addEventListener("click",function(event) {
alert("Trikitrakatelas")
})


//Evento mouseover que nos da un alert cada vez que pasamos el mouse por encima del titulo
const encabezado = document.getElementById("tituloh1")
encabezado.addEventListener("mouseover", () => {
    alert("halloooo")
})

//Boton de cambio de color que nos cambia el color del titulo
const changeColor = document.getElementById("change-color")

changeColor.addEventListener("click", function(event){
    const R = randomNumber().toString()
    const G = randomNumber().toString()
    const B = randomNumber().toString()

    encabezado.style.color = `rgb(${R},${G},${B})`

})

function randomNumber(){
    return (Math.random()*256).toFixed(0)
}   

//Ejercitación

let concat = document.getElementById("concatenar");

concat.addEventListener("click",function(event){
    const texto1 = document.getElementById("primer_texto").value
    const texto2 = document.getElementById("segundo_texto").value
    alert(`${texto1} ${texto2}`)
})