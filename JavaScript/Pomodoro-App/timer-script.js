const bells = new Audio('./sounds/bell.wav'); 
// Feature Buttons
const startBtn = document.querySelector('.btn-start');
const resetBtn = document.querySelector('.btn-reset');
const setTimerBtn = document.querySelector('.btn-set-time');
// Pause Button
const pauseBtn = document.createElement('button');
pauseBtn.className = "btn-pause timer-btn";
pauseBtn.textContent = "pause";
// HTML Timer
const sessionMin = document.querySelector('.minutes');
const sessionSec = document.querySelector('.seconds');
// Global variable for Set Time func
let updateMin = 1;

// Interval State
let myInterval;
let timerOff = true; // true = off, false = on

const pomodoroTimer = () => {
    const sessionAmount = (Number.parseInt(sessionMin.textContent) * 60) + (Number.parseInt(sessionSec.textContent));

    if(timerOff) {
        timerOff = false;
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
};

startBtn.addEventListener('click', function() {
    // Replace Play Button with Pause
    startBtn.parentNode.replaceChild(pauseBtn, startBtn);
    pomodoroTimer();
});

// Pause Timer
pauseBtn.addEventListener('click', () => {
    clearInterval(myInterval);
    timerOff = true;
    pauseBtn.parentNode.replaceChild(startBtn, pauseBtn);
});

setTimerBtn.addEventListener('click', function() {
    clearInterval(myInterval);
    if(timerOff) { // Off
        pauseBtn.parentNode.replaceChild(startBtn, pauseBtn); // Pause -> Start
    } else { // On
        timerOff = true;
        pauseBtn.parentNode.replaceChild(startBtn, pauseBtn); // Pause -> Start
    }

    // Prompt
    updateMin = parseInt(prompt("Edit Time:", sessionMin.textContent));
    
    // Error Checking
    while (isNaN(updateMin) || (updateMin === 0)) { // Cannot start at 0
        updateMin = parseInt(prompt("This is not valid. Please enter a number for the timer.", ""))
    }

    // Set Timer
    sessionMin.textContent = updateMin;
    sessionSec.textContent = '00';
});

// Reset Time
resetBtn.addEventListener('click', function() {
    clearInterval(myInterval);
    if(timerOff) { // Off
        pauseBtn.parentNode.replaceChild(startBtn, pauseBtn); // Pause -> Start
    } else { // On
        timerOff = true;
        pauseBtn.parentNode.replaceChild(startBtn, pauseBtn); // Pause -> Start
    }

    // Set timer
    if(updateMin === 1) { // Default
        sessionMin.textContent = 1;
        sessionSec.textContent = '00';
    } else { // Updated time
        sessionMin.textContent = updateMin;
        sessionSec.textContent = '00';
    }
});