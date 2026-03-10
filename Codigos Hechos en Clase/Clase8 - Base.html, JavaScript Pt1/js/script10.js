
const greet = function (valor) {
    return function () {
        console.log("Bienvenido a nuestra materia,",valor);
    }
}
greet("Juan")();

