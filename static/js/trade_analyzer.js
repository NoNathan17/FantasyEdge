document.addEventListener('DOMContentLoaded', function() {
    const tradeForm = document.getElementById('tradeForm');
    const resultContainer = document.getElementById('resultContainer');
    const resultText = document.getElementById('resultText');

    resultText.textContent = '';
    resultContainer.style.display = 'none';

    tradeForm.addEventListener('submit', function(event) {
        event.preventDefault(); 

        const player1 = document.getElementById('player_1').value.trim();
        const player2 = document.getElementById('player_2').value.trim();
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        if (!player1 || !player2) {
            resultText.textContent = "Both player names are required.";
            resultContainer.style.display = 'block';
            return;
        }

        fetch('/compare/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': csrfToken,
            },
            body: new URLSearchParams({
                'player_1': player1,
                'player_2': player2
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.result) {
                resultText.textContent = data.result;
                resultContainer.style.display = 'block';
            } else if (data.error) {
                resultText.textContent = data.error;
                resultContainer.style.display = 'block';
            }
        })
        .catch(error => {
            resultText.textContent = "An error occurred. Please try again.";
            resultContainer.style.display = 'block';
        });
    });
});
