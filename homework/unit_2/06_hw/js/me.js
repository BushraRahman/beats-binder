"use strict"

document.querySelector(".button_check").addEventListener("click", function() {
    console.log("The button has been clicked");
});
let bg_change_times = 0; // Initialize a variable
document.querySelector(".button_css").addEventListener("click", function() {
    let input_element_style=document.querySelector(".game_selector").style;
    if (input_element_style.backgroundColor==="red") {
        input_element_style.backgroundColor="";
    } else if (input_element_style.backgroundColor===""){input_element_style.backgroundColor="red";}
    bg_change_times++;
    document.querySelector(".bg_info").textContent=`How many times have we changed the background ${bg_change_times}`;
});


document.querySelector(".button_class").addEventListener("click", function() {
        let input_element_style=document.querySelector(".boo").classList;
        if (input_element_style.contains("hidden")) {
            input_element_style.remove("hidden");
        } else {input_element_style.add("hidden");}
    });

document.addEventListener('keydown', function() {
    if (document.activeElement != document.querySelector(".game_selector")) {
        if (event.key=="r"){
    console.log(`a key was pressed ${event.key}`)
        }
    }
})

let game_list = [{'name': 'hyper demon'}]
const containerParentGameList = document.querySelector('.game_list_container')

const addGameList = function (listElement, game) {
    const li_element = document.createElement('li');
    li_element.innerHTML = game.name;
    listElement.insertAdjacentElement('beforeend', li_element);
}

const containerGameList = document.createElement('ul');
containerGameList.classList.add('game_list');
for (const game of game_list) {
    addGameList(containerGameList, game);
}
containerParentGameList.insertAdjacentElement('beforeend', containerGameList);

document.querySelector(".change_color").addEventListener("click", function() {
    document.documentElement.style.setProperty('--primary-color', 'red');
})

const eventFunc =  function(event){
    console.log("mous epassed over fiv aoisud");
}

containerGameList.addEventListener('mouseenter', eventFunc);
setTimeout(()=>containerGameList.removeEventListener('mouseenter', eventFunc), 10000);

class Student {
    constructor(firstName, lastName, schoolClass) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.schoolClass = schoolClass;
    }
    
    saveGrade(grade, curve) {
        grade = grade + curve;
        if (grade > 100) {
            this.grade = 100;
        } else if (grade < 0 ) {
            this.grade = 0;
        }
    }
    get latest(){
        return this.grades.slice(-1)
    }
    set latest(grade){
        this.grades.push(grade)
    }
}

Student.prototype.saysHi = function() {
    console.log(this.firstName, this.lastName, "says hi!!!");
}

const grade_object = {
    'student': 'Kate',
    'grades' : [95,90,98],
    get latest(){
        return this.grades.slice(-1)
    },
    set latest(grade){
        this.grades.push(grade)
    }
}

class Animal {
    constructor(name, favFood) {
        this.name = name;
        this.food = favFood;
    }
    identifier(){
        return `I am ${name}`;
    }
}

class Dog extends Animal {
    constructor(name, favFood, sound) {
        super(name, favFood);
        this.sound = sound;
    }
    makeNoise(){
        let doubleSound = this.sound + this.sound;
        return doubleSound;
    }
}

class Poodle extends Dog {
    constructor(name, favFood, sound) {
        super(name, favFood);
        this.sound = sound;
    }
    makeNoise(){
        let doubleSound = super.makeNoise() + ", moving the tail";
        console.log(doubleSound);
        return doubleSound;
    }
}

const barky = new Poodle('barky', 'marrow', 'woof')
barky.makeNoise();


// const ariana = new Student('Ariana', 'Smith', '7th grade');
// ariana.saveGrade(95, 10);

// const Car = function(brand, speed) {
//     this.brand = brand;
//     this.speed = speed;

//     this.accelerate = function(speedAdder) {
//         this.speed = this.speed + speedAdder;
//         console.log(this.speed);
//     }
//     this.brake = function(speedSubtractor) {
//         this.speed = this.speed - speedSubtractor;
//         console.log(this.speed);
//     }
// }

const Car = function(make, speed) {
    this.make = make;
    this.speed = speed;
}

Car.static_method = function(){
    console.log("I AM A STATIC METHOD");
}

Car.static_method();

const car1 = new Car('audi', 130);
const car2 = new Car('renault', 100);


// const addGameList = function (game) {
//     const html = `<li>${game.name}</li>`;
//     containerGameList.insertAdjacentHTML('afterend', html);
// }

// for (const game of game_list){
//     addGameList(game);
// }