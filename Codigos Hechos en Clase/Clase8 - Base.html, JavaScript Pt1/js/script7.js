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