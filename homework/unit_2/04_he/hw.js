// function calcAge1(birthYear){
//     return 2023 - birthYear;
// }

// const calcAge2 = function(birthYear){
//     return 2023 - birthYear;
// }

// const calcAge3 = birthYear => 2023 - birthYear;
const calcAverage = (score1, score2, score3) => { return (score1 + score2 + score3) / 3 };

let scoreDolphins = calcAverage(44,23,71);
let scoreKoalas = calcAverage(65, 54, 49);

//let scoreDolphins = calcAverage(85,54,41);
//let scoreKoalas = calcAverage(23, 34, 27);

function checkWinner(avgDolphins, avgKoalas) {
    if (avgDolphins > avgKoalas) {
        console.log(`Dolphins win (${scoreDolphins} , ${scoreKoalas})`);
    } else if (avgKoalas > avgDolphins) {
        console.log(`Koalas win (${scoreKoalas} , ${scoreDolphins})`);
    } else {
        console.log("No team wins")
    }
}

checkWinner(scoreDolphins, scoreKoalas);

// const age2 = calcAge2(1991);
// const age1 = calcAge1(1991);
// const age3 = calcAge3(1991);

//console.log(age1, age2, age3);