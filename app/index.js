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

document.addEventListener("DOMContentLoaded", function() {
    const radioButtons = document.querySelectorAll('input[name="result_system"]');
    const customInput = document.getElementById('customResultInput');

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

function convertNumber() {
    var inputNumber = document.getElementById("inputNumber").value.trim();

    var startSystem = document.querySelector("input[name='number_system']:checked").value;
    startSystem = getNumericSystem(startSystem);
    if (startSystem === "custom") {
        startSystem = document.getElementById("customValue").value.trim();
        startSystem = parseInt(startSystem)
    }

    var resultSystem = document.querySelector("input[name='result_system']:checked").value;
    resultSystem = getNumericSystem(resultSystem);
    if (resultSystem === "custom") {
        resultSystem = document.getElementById("customResultValue").value.trim();
        resultSystem = parseInt(resultSystem)
    }
    
    var decimalNumber = parseInt(inputNumber, startSystem);

    var convertedNumber = decimalNumber.toString(resultSystem);

    document.getElementById("outputResult").textContent = convertedNumber;
}

function getNumericSystem(systemName) {
    switch (systemName) {
        case "binary":
            return 2;
        case "ternary":
            return 3;
        case "octal":
            return 8;
        case "decimal":
            return 10;
        case "hexadecimal":
            return 16;
        case "custom":
            return "custom";
        default:
            return 10;
    }
}

document.getElementById("convertButton").addEventListener("click", convertNumber);