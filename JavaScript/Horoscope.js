// JavaScript Checkpoint - Horoscope
console.log("✨ Welcome~ Have you ever wondered what your future holds?\n");

// Random Birth Month - Define Variable
// We can input it manually by getting rid of the random generator for birthMonth variable
const monthArray = [
  "January", "February", "March", 
  "April", "May", "June", "July", 
  "August", "September", "October", 
  "November", "December"
];

let birthMonth = monthArray[Math.floor(Math.random () * 12)];
console.log("🔮 Your birth month is", birthMonth, "~~");
console.log("💌 Let's see your horoscope & future!\n");

// Fortune Messages
const fortuneArray = [
  "You will find a sock missing from every laundry load.",
  "You will soon discover that your pet understands more than you think.",
  "You will find something you lost in the last place you look. Always.",
  "A thrilling time is in your immediate future. Don't forget the snacks.",
  "You will conquer the pile of laundry tomorrow... or at least move it around.",
  "You will be hungry again in one hour.",
  "That wasn't chicken.",
  "Your life will be happy and peaceful... until your internet connection goes down.",
  "Avoid taking unnecessary gambles. Lucky numbers: 1, 1, 1, 1, 1, 1.",
  "Your pet is planning to take over the world. Beware.",
  "Your future holds a nap that feels like a mini-vacation.",
  "This cookie contains 117 calories. Enjoy wisely.",
  "An unexpected shower of good luck is coming. Bring an umbrella.",
  "You will soon realize that the remote was in your hand all along.",
  "You will soon receive a compliment. Don’t let it go to your head.",
  "Good news will come to you by mail... probably junk mail, but still!"
];

// Randomly print a fortune
let fortuneMsg = fortuneArray[Math.floor(Math.random () * 16)];

if (birthMonth == "January") {
  console.log("=== ♑ Capricorn Fortune ♑ ===");
  console.log(fortuneMsg);
} else if (birthMonth == "February") {
  console.log("=== ♒ Aquarius Fortune ♒ ===");
  console.log(fortuneMsg);
} else if (birthMonth == "March") {
  console.log("=== ♓ Pisces Fortune ♓ ===");
  console.log(fortuneMsg);
} else if (birthMonth == "April") {
  console.log("=== ♈ Aries Fortune ♈ ===");
  console.log(fortuneMsg);
} else if (birthMonth == "May") {
  console.log("=== ♉ Taurus Fortune ♉ ===");
  console.log(fortuneMsg);
} else if (birthMonth == "June") {
  console.log("=== ♊ Gemini Fortune ♊ ===");
  console.log(fortuneMsg);
} else if (birthMonth == "July") {
  console.log("=== ♋ Cancer Fortune ♋ ===");
  console.log(fortuneMsg);
} else if (birthMonth == "August") {
  console.log("=== ♌ Leo Fortune ♌ ===");
  console.log(fortuneMsg);
} else if (birthMonth == "September") {
  console.log("=== ♍ Virgo Fortune ♍ ===");
  console.log(fortuneMsg);
} else if (birthMonth == "October") {
  console.log("=== ♎ Libra Fortune ♎ ===");
  console.log(fortuneMsg);
} else if (birthMonth == "November") {
  console.log("=== ♏ Scorpio Fortune ♏ ===");
  console.log(fortuneMsg);
} else if (birthMonth == "December") {
  console.log("=== ♐ Sagittarius Fortune ♐ ===");
  console.log(fortuneMsg);
} else {
  console.log("Not a valid month. Try again!")
}