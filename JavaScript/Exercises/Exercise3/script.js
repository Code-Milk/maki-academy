let getStone = document.getElementById("stone");
let randomNumber = Math.floor(Math.random(9) * 10) +1;

if(randomNumber == 1) {
    getStone.style.backgroundColor = "red";
} else if (randomNumber == 2) {
    getStone.style.backgroundColor = "orange";
} else if (randomNumber == 3) {
    getStone.style.backgroundColor = "yellow";
} else if (randomNumber == 4) {
    getStone.style.backgroundColor = "green";
} else if (randomNumber == 5) {
    getStone.style.backgroundColor = "blue";
} else if (randomNumber == 6) {
    getStone.style.backgroundColor = "#4169e1";
} else if (randomNumber == 7) {
    getStone.style.backgroundColor = "#00008b";
} else if (randomNumber == 8) {
    getStone.style.backgroundColor = "purple";
} else {
    getStone.style.backgroundColor = "black";
} 