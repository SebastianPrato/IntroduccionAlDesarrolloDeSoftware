function student(){
    return "Alumno";
}
function greet(user){
    console.log("Bienvenido", user());    
}
    // Prints "Bienvenido Alumno"
let message = greet(student);