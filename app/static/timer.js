/* TRICK: We check if INITIAL_TIME is defined (from the HTML).
   If yes, use it. If no (e.g. testing file directly), default to 25.
*/
let sessionDuration = (typeof INITIAL_TIME !== 'undefined') ? INITIAL_TIME : 25;

let mode = true //True = focus mode | False = break time
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
    document.title = `(${minutes}:${seconds < 10 ? '0' : ''}${seconds}) ${mode ? 'Focus' : 'Break'}`;
}

function breakTimer() {
    alert("Focus session complete! Take a break. ☕");

    timeLeft = sessionDuration / 5 * 60;
    timerId = setInterval(() => {
        timeLeft--;
        updateDisplay()
    }, 1000)
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
            if (mode) {
                // Switch to break mode
                clearInterval(timerId);
                mode = false;
                timeLeft = Math.floor(sessionDuration / 5) * 60; // 5-minute break
                updateDisplay();
                alert("Focus session complete! Take a break. ☕");
                // Start break timer
                timerId = setInterval(() => {
                    timeLeft--;
                    updateDisplay();
                    if (timeLeft <= 0) {
                        // Break over, reset to focus and continue cycle
                        clearInterval(timerId);
                        isRunning = false;
                        startBtn.textContent = "Start Focus";
                        mode = true;
                        timeLeft = sessionDuration * 60;
                        updateDisplay();
                        alert("Break time over! Back to focus. 📚");
                        // Automatically start next focus session
                        startTimer();
                    }
                }, 1000);
            }
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
    mode = true;
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