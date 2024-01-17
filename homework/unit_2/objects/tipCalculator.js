function calcTip(billValue) {
    if (billValue >= 50 && billValue <= 300) {
        return billValue * .15;
    } else {
        return billValue * .2;
    }
}

bills = [125, 555, 44];
tips = [];
totals = [];

for (bill of bills) {
    tip = calcTip(bill);
    tips.push(tip);
    totals.push(bill + tip);

}

console.log(tips, totals);