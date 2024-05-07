document.addEventListener("DOMContentLoaded", function() {
    const radioButtons = document.querySelectorAll('input[name="number_system"]');
    const customInput = document.getElementById('customInput');

    radioButtons.forEach(function(radioButton) {
        radioButton.addEventListener('change', function() {
            if (this.value === 'custom') {
                customInput.style.display = 'block';
            } else {
                customInput.style.display = 'none';
            }
        });
    });
});
