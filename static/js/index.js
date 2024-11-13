// Function to clear messages after a delay
function clearMessages() {
    const messages = document.querySelectorAll('.message');
    
    messages.forEach(function(message, index) {
        const delay = 1000 * (index + 1); // Customize delay for each message
        setTimeout(function() {
            message.style.display = 'none';
        }, delay);
    });
}

window.onload = function() {
    clearMessages();
};
