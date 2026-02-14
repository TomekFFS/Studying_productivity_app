/* TRICK: We check if INITIAL_TIME is defined (from the HTML).
   If yes, use it. If no (e.g. testing file directly), default to 25.
*/
let sessionDuration = (typeof INITIAL_TIME !== 'undefined') ? INITIAL_TIME : 25;

let timeLeft = sessionDuration * 60; 
let timerId = null;
let isRunning = false;

const display = document.getElementById('timer-display');
const startBtn = document.getElementById('start-btn');
const resetBtn = document.getElementById('reset-btn');

// Initialize display immediately so user sees "25:00" (or 50:00) right away
updateDisplay();

function updateDisplay() {
    const minutes = Math.floor(timeLeft / 60);
    const seconds = timeLeft % 60;
    // Add leading zeros (e.g., 9 -> 09)
    display.textContent = `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
    document.title = `(${minutes}:${seconds < 10 ? '0' : ''}${seconds}) Focus`;
}

function startTimer() {
    if (isRunning) return;

    isRunning = true;
    startBtn.textContent = "Pause";
    startBtn.style.backgroundColor = "var(--danger-color)"; // Visual feedback

    timerId = setInterval(() => {
        timeLeft--;
        updateDisplay();

        if (timeLeft <= 0) {
            clearInterval(timerId);
            isRunning = false;
            startBtn.textContent = "Finished!";
            alert("Focus session complete! Take a break. ☕");
        }
    }, 1000);
}

function pauseTimer() {
    clearInterval(timerId);
    isRunning = false;
    startBtn.textContent = "Resume";
    startBtn.style.backgroundColor = ""; // Reset color
}

function resetTimer() {
    pauseTimer();
    // RESET logic: Go back to the original session duration
    timeLeft = sessionDuration * 60;
    startBtn.textContent = "Start Focus";
    updateDisplay();
}

// Event Listeners
startBtn.addEventListener('click', () => {
    if (isRunning) {
        pauseTimer();
    } else {
        startTimer();
    }
});

resetBtn.addEventListener('click', resetTimer);