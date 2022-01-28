
var nombre = "Víctor Robles";
var altura = 189;
var concatenacion = nombre + ' ' + altura
/*
document.write(nombre);
document.write(altura);
document.write(concatenacion);

var datos = document.getElementById("datos")
datos.innerHTML = concatenacion
datos.innerHTML += `
    <h1>Soy la caja de datos</h1>
    <h2>Mi nombre es: ${nombre}</h2>
    <h3>Mido: ${altura}cm</h3>
`
if(altura >= 190){
    datos.innerHTML += `
        <h1>Eres una persona alta</h1>
    `}

for(var i=2000; i<=2020; i++){
    datos.innerHTML += `
    <h2>Es el año: </h2>
        <p>${i}</p>
    `
}
*/
function imprimir(nombre, altura){
    var datos = document.getElementById("datos");
    datos.innerHTML = MuestraMiNombre(nombre,altura);
}

function MuestraMiNombre(nombre, altura) {
    
    var misDatos = `
    <h1>Soy la caja de datos</h1>
    <h2>Mi nombre es: ${nombre}</h2>
    <h3>Mido: ${altura}cm</h3>
    `;

    return misDatos;
}

imprimir('Víctor Robles WEB', 111);

var nombres = ['Víctor', 'Antonio', 'Joaquín'];
/*
for(var i = 0; i < nombres.length; i++){
    var datos = document.getElementById("datos");
    datos.innerHTML += `
        <p>${nombres[i]}</p>
    `;

}
*/
/*
nombres.forEach(function(nombre){
    var datos = document.getElementById("datos");
    datos.innerHTML += `
        <p>${nombre}</p>
    `;
});
*/
nombres.forEach(nombre => {
    var datos = document.getElementById("datos");
    datos.innerHTML += `
        <p>${nombre}</p>
    `;
});