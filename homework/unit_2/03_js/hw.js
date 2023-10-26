//1
semiPerimeter = (5+6+7)/2
console.log("1.")
console.log(Math.sqrt(semiPerimeter *(semiPerimeter -5)*(semiPerimeter -6)*(semiPerimeter -7)))
console.log()
//2
const date = new Date()
let day;
switch (date.getDay()) {
    case 0:
        day = "Sunday"
    break;
    case 1:
        day = "Monday"
    break;
    case 2:
        day = "Tuesday"
    break;
    case 3:
        day = "Wednesday"
    break;
    case 4:
        day = "Thursday"
    break;
    case 5:
        day = "Friday"
    break;
    case 6:
        day = "Saturday"
    break;
}
console.log("2.")
console.log("Sample Output: Today is: " + day)
console.log("Current time is: "+ date.toLocaleTimeString())
console.log()

//3.

console.log("3.")
let input = prompt("PUT IN A RANDOM NUMBER")
if (input == Math.floor(Math.random() * 10)){
    console.log("Good Work")
} else {console.log("Not Matched")}
console.log()

//4.
input = prompt("PUT IN CELCIUS")
console.log("4.")
console.log((input * (9/5))+32)
console.log()

//5.

let message = "chicken"
console.log("5.")
if (message.length < 5){
    console.log("MESSAGE LESS THAN 5 CHARACTERS")
} else{
prior = message.substring(0, 5-1)
after = message.substring(5, message.length)
console.log(prior + after);
}
console.log()