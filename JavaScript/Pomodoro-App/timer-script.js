const bells = new Audio('./sounds/bell.wav'); 
const startBtn = document.querySelector('.btn-start');
const resetBtn = document.querySelector('.btn-reset');
const setTimerBtn = document.querySelector('.btn-set-time');
const sessionMin = document.querySelector('.minutes');
const sessionSec = document.querySelector('.seconds');

let myInterval;
let pausedInterval;
let state = true; // true = off, false = on

startBtn.addEventListener('click', function() {
    const sessionAmount = (Number.parseInt(sessionMin.textContent) * 60) + (Number.parseInt(sessionSec.textContent));

    // Replace Play Button with Pause
    const pauseBtn = document.createElement('button');
    pauseBtn.className = "btn-pause timer-btn";
    pauseBtn.textContent = "pause";
    startBtn.parentNode.replaceChild(pauseBtn, startBtn);

    // Pause Timer
    pauseBtn.addEventListener('click', () => {
        clearInterval(myInterval);
        state = true;
        pauseBtn.parentNode.replaceChild(startBtn, pauseBtn);
    });

    if(state) {
        state = false;
        let totalSeconds = sessionAmount;

        const updateSeconds = () => {
            const minuteDiv = document.querySelector('.minutes');
            const secondDiv = document.querySelector('.seconds');
        
            totalSeconds--;
        
            let minutesLeft = Math.floor(totalSeconds/60);
            let secondsLeft = totalSeconds % 60;
        
            if(secondsLeft < 10) {
                secondDiv.textContent = '0' + secondsLeft;
            } else {
                secondDiv.textContent = secondsLeft;
            }
            
            minuteDiv.textContent = `${minutesLeft}`
        
            if(minutesLeft === 0 && secondsLeft === 0) {
                bells.play()
                clearInterval(myInterval);
            }
        }
        myInterval = setInterval(updateSeconds, 1000);
    } else {
        alert('Session has already started.')
    }
});

setTimerBtn.addEventListener('click', function() {
    const setTimerMin = document.querySelector('.minutes');
    const setTimerSec = document.querySelector('.seconds');

    // Prompt
    let updateMin = parseInt(prompt("Edit Time:", setTimerMin.textContent));

    // Error Checking
    while (isNaN(updateMin)) {
        updateMin = parseInt(prompt("This is not a number. Please enter a number for the timer.", ""))
    }
    
    // Set
    setTimerMin.textContent = updateMin;
    setTimerSec.textContent = '00';

    // Reset Time
    resetBtn.addEventListener('click', function() {
        setTimerMin.textContent = updateMin;
        setTimerSec.textContent = '00';
    });
});