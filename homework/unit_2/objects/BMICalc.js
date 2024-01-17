const mark = {
    fullName: "Mark Miller",
    mass: 78,
    height: 1.69,
    calcBMI: function() {
        return this.mass / (this.height ** 2);
    },
}

const john = {
    fullName: "John Smith",
    mass: 92,
    height: 1.95,
    calcBMI: function() {
        return this.mass / (this.height ** 2);
    },
}

let bigBoy;
let smallBoy;

if (john.calcBMI() > mark.calcBMI()) {
    bigBoy = john;
    smallBoy = mark;
} else {
    bigBoy = mark;
    smallBoy = john;
}

console.log(`${bigBoy.fullName}'s BMI (${bigBoy.calcBMI()}) is higher than ${smallBoy.fullName}'s BMI (${smallBoy.calcBMI()})`);
