

let timeLeft = 25 * 60; // 25 minutes
let timerId = null;
let isRunning = false;

const display = document.getElementById('timer-display');
const startBtn = document.getElementById('start-btn');
const resetBtn = document.getElementById('reset-btn');

function updateDisplay() {
    const minutes = Math.floor(timeLeft / 60);
    const seconds = timeLeft % 60;
    display.textContent = `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
    document.title = `(${minutes}:${seconds < 10 ? '0' : ''}${seconds}) Focus`;
}

function startTimer() {
    if (isRunning) return;

    isRunning = true;
    startBtn.textContent = "Pause";
    // We can change style via class or direct style.
    // Let's stick to simple logic here.
    startBtn.style.backgroundColor = "var(--danger-color)";

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
    startBtn.style.backgroundColor = ""; // Reset to default CSS
}

function resetTimer() {
    pauseTimer();
    timeLeft = 25 * 60;
    startBtn.textContent = "Start Focus";
    updateDisplay();
}

startBtn.addEventListener('click', () => {
    if (isRunning) {
        pauseTimer();
    } else {
        startTimer();
    }
});

resetBtn.addEventListener('click', resetTimer);

// Init
updateDisplay();