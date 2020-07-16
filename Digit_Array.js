var userNumberArray = ['0', '0', '0', '0']; //empty array of 0's as this value is not allowed, this array will store the computers auto-generated number
        var availableNumbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] //array of available numbers to be picked and added to the computerNumber array
        


//this function is used later to calculate the possible permutations of combinations of user guess
function factorial(x) {
    if (x === 0) { return 1; }
    else{
        return x * factorial(x-1);
    }
}


function arrayCreate(availableNumbers, userNumberArray) {

    var possibleValues = []; //empty array to house all the possible combination of values that the user could enter i.e. 1234 to 9876
    var numberOfPermutations = (factorial(availableNumbers.length) / factorial(availableNumbers.length - userNumberArray.length));

    var adding = true;
    var firstDigit, secondDigit, thirdDigit, forthDigit =0;
    var possibleDigitValue = "";


    while (adding === true) {
        for (var i = 0; i < availableNumbers.length; i++) {
            firstDigit = availableNumbers[i];
            availableNumbers.splice(i, 1);
            for (var j = 0; j < availableNumbers.length; j++) {
                secondDigit = availableNumbers[j];
                availableNumbers.splice(j, 1);
                for (var k = 0; k < availableNumbers.length; k++) {
                    thirdDigit = availableNumbers[k]
                    availableNumbers.splice(k, 1);
                    for (var l = 0; l < availableNumbers.length; l++) {
                        forthDigit = availableNumbers[l];
                        possibleDigitValue = (firstDigit + secondDigit + thirdDigit + forthDigit);
                        possibleValues.push(possibleDigitValue);
                    }
                    availableNumbers.splice(k, 0, thirdDigit);
                }
                availableNumbers.splice(j, 0, secondDigit);
            }
            availableNumbers.splice(i, 0, firstDigit);
            if (possibleValues.length >= numberOfPermutations) {
                adding = false;
            }
        }
        return possibleValues;
    }
}
console.log(arrayCreate(availableNumbers, userNumberArray));
