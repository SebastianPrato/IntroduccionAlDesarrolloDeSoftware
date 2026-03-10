//Mostrar contenido por consola

console.log("aaaa")

//If

let numero = 8

if (numero < 20) {
    console.log("El número es menor a 20")
} else if (numero == 20) {
    console.log("El número es igual a 20")
} else {
    console.log("El número es mayor a 20")
}

//Ciclos

while (numero < 20) {
    numero++  // numero = numero + 1
    console.log(numero)
}

for (let i=1; i<5; i++) {
    const nuevoValor = numero + i
    console.log("Ahora el número vale: " + nuevoValor)
}


//Switch

const color = "red"

switch(color) {
    case "red": {
        console.log("El color es rojo")
        break
    }
    case "blue": {
        console.log("El color es azul")
        break
    }
    case "yellow": {
        console.log("El color es amarillo")
        break
    }
    default: {
        console.log("El color no existe")
    }    
}


//Concatenación

const nombre = "Pepito"
const apellido = "Perez"

// Usando el operador +
const fullName1 = nombre + " " + apellido

// Usando template literals
const fullName2 = `${nombre} ${apellido}`

console.log(fullName1) // Pepito Perez
console.log(fullName2) // Pepito Perez  

//Arreglos

const nombres = ["Juan", "Pedro", "María", "Ana", "Luis"]

    // Usando un bucle for
for (let i = 0; i < nombres.length; i++) {
    console.log(nombres[i])
}

    // Usando un bucle forEach
nombres.forEach(function(nombre) {
    console.log(nombre)
})

    // Usando un bucle for...of
for (const nombre of nombres) {
    console.log(nombre)
}

//Objetos

const persona = {
    name: "Pepito Perez",
    edad: 24,
    "ciudad de origen": "Buenos Aires"
}
  
console.log(typeof persona) // object
  
    // recorrer el objeto persona
for (let key in persona) {
    console.log(`clave: ${key} / valor: ${persona[key]}`)
}
  
    // convertir el objeto persona a un string
const personaString = JSON.stringify(persona)
console.log(personaString)
  
    // convertir el string a un objeto
const personaObjeto = JSON.parse(personaString)
console.log(personaObjeto)
  

//Funciones como tipo de dato:

const numeros = [1, 2, 3, 4, 5, 6]
const filtrados = numeros.filter(x => x % 2 == 0)
console.log(filtrados)  // resultado: [2, 4, 6]


//Funciones como parámetro:

function student(){
    return "Alumno";
}
function greet(user){
    console.log("Bienvenido", user());    
}
    // Prints "Bienvenido Alumno"
let message = greet(student);


//Funciones como resultado de otra función:

const greet = function (valor) {
    return function () {
        console.log("Bienvenido a nuestra materia,",valor);
    }
}
greet("Juan")();

