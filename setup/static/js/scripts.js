const toggleButton = document.getElementById('darkMode');

toggleButton.addEventListener('click', () => {
    document.body.classList.toggle('darkMode');
    
    
    if (document.body.classList.contains('darkMode')) {
        toggleButton.textContent = "☀️";
    } else {
        toggleButton.textContent = "🌙";
    }
}
);
