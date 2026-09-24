//Introduction to Javascript. 
// commenting

/* Multiline comments
efhoweughw
shfgasif
*/

//console log
console.log('Hello Javascript')

// numbers 
let number = 68;
let price = 44.89;

//let total = price + number;

console.log(number, price, number + price)

// variables

let x = null;
let name = "Locke"
const found = true;

console.log(name, found, x)

// strings 
let single = 'This is a single string';
let double = "This is a double string"

console.log(single.length, double.length)

// Arithmetic opertaions
let add1 = 12 + 24 //addition
let sub1 = 10 - 6 //substraction
let mult1 = 5 * 5 //multiplication
let div1 = 100  / 25 //division
let total = add1 + sub1 + mult1 + div1  

console.log("Result", add1, sub1, mult1, div1, total)

// Assignment operators 
let numberone = 100;
numbertwo = numberone + 15
console.log(numbertwo)
numberone += 15; 
console.log(numberone)

//string Operations

//string concatenation
let age = 20;
console.log('John is ' + age + ' years old')

// Javascript Conditions
// If conditions

const isNameLocke = true;

if (isNameLocke) {
   console.log("Name is Locke");
}

//else  if conditions
const size = 101;
if (size > 100){
    console.log("Big");
} else if ( size > 20){
    console.log("Medium")
} else if (size > 4){
    console.log("Small")
} else {
    console.log("Tiny")
}
