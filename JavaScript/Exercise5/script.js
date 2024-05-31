const memeArray = [
    "https://i.pinimg.com/474x/9d/d4/52/9dd45271b020a094a12bfeee12b39f65.jpg",
    "https://i.pinimg.com/474x/93/27/4a/93274a283265b837079617dd30c3f110.jpg",
    "https://i.pinimg.com/474x/bb/ae/6b/bbae6b3900ab9baef27480c8f578b989.jpg",
    "https://i.pinimg.com/474x/27/89/6f/27896fe6c2e52d75ecfa6470bbccb540.jpg",
    "https://i.pinimg.com/474x/42/f1/05/42f1054c46f5d2b2382a540ddd86d716.jpg",
    "https://i.pinimg.com/474x/45/79/b7/4579b710ccc853ba1256575c22ecf96a.jpg",
    "https://i.pinimg.com/474x/27/02/b5/2702b536d2a8afb02082fc854cecb0f4.jpg",
    "https://i.pinimg.com/474x/ca/c7/81/cac781a76e5f4ab5219625d07b9ef533.jpg",
    "https://i.pinimg.com/474x/b0/46/de/b046dea6c2e104496d78fe55f148ffdf.jpg",
    "https://i.pinimg.com/474x/69/02/cd/6902cd3556639678ffb92bb58770d7ba.jpg",
    "https://i.pinimg.com/474x/a7/a3/74/a7a374973c99beea8b3f7c76034de984.jpg"
];

const captionsArray = [
  "Wakeup and makeup",
  "I need a vacation so long, I forget all my passwords",
  "My blood is made of coffee.",
  "Money cannot buy happiness. But it can buy Makeup!",
  "Friendly faces from around the world.",
  "Never stop doing things for the first time.",
  "I know I left my sanity around here somewhere.",
  "To be at one with nature is to be content with life.",
  "Vodka may not be the answer but it is worth a shot."
];

let getRandomMeme = document.getElementById("random-meme");
let getRandomCaption = document.getElementById("random-caption");
let getGeneratorButton = document.getElementById("generator-button");

getGeneratorButton.addEventListener("click", function() {
    let randomIndex1 = Math.floor(Math.random() * memeArray.length);
    let randomIndex2 = Math.floor(Math.random() * captionsArray.length);

    getRandomMeme.src = memeArray[randomIndex1];
    getRandomCaption.innerText = captionsArray[randomIndex2];
});