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