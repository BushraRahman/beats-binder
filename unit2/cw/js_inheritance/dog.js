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

const barky = new Poodle('barky', 'chocolate', 'woof')
barky.makeNoise();