document.addEventListener('DOMContentLoaded', function () {
    const tradeForm = document.getElementById('tradeForm');
    const resultContainer = document.getElementById('resultContainer');
    const resultText = document.getElementById('resultText');
    const addGivingPlayerButton = document.getElementById('addGivingPlayer');
    const addGettingPlayerButton = document.getElementById('addGettingPlayer');
    const givingPlayersContainer = document.getElementById('givingPlayersContainer');
    const gettingPlayersContainer = document.getElementById('gettingPlayersContainer');

    resultText.textContent = '';
    resultContainer.style.display = 'none';

    addGivingPlayerButton.addEventListener('click', function () {
        const inputContainer = document.createElement('div');
        inputContainer.classList.add('player-input-container');
        inputContainer.innerHTML = `
            <input type="text" name="giving[]" class="player-input" placeholder="Player search..." autocomplete="off">
        `;
        givingPlayersContainer.appendChild(inputContainer);
    });

    addGettingPlayerButton.addEventListener('click', function () {
        const inputContainer = document.createElement('div');
        inputContainer.classList.add('player-input-container');
        inputContainer.innerHTML = `
            <input type="text" name="getting[]" class="player-input" placeholder="Player search..." autocomplete="off">
        `;
        gettingPlayersContainer.appendChild(inputContainer);
    });

    document.addEventListener('input', function (event) {
        if (event.target.classList.contains('player-input')) {
            const input = event.target;
            const query = input.value.trim();

            let dropdown = input.nextElementSibling;
            if (!dropdown || !dropdown.classList.contains('trade-dropdown')) {
                dropdown = document.createElement('ul');
                dropdown.classList.add('trade-dropdown');
                input.parentNode.appendChild(dropdown);
            }

            if (query.length > 0) {
                fetch(`/autocomplete/?term=${encodeURIComponent(query)}`)
                    .then(response => response.json())
                    .then(data => {
                        dropdown.innerHTML = '';
                        if (data.players.length > 0) {
                            data.players.forEach(player => {
                                const suggestion = document.createElement('li');
                                suggestion.textContent = player;
                                suggestion.classList.add('trade-dropdown-item');
                                suggestion.addEventListener('click', function () {
                                    input.value = player; // Set input value to selected suggestion
                                    dropdown.innerHTML = ''; // Clear the dropdown
                                });
                                dropdown.appendChild(suggestion);
                            });
                        }
                    })
                    .catch(error => console.error("Error fetching suggestions:", error));
            } else {
                dropdown.innerHTML = ''; 
            }
        }
    });

    tradeForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        const givingPlayers = Array.from(document.querySelectorAll('input[name="giving[]"]')).map(input => input.value.trim()).filter(Boolean);
        const gettingPlayers = Array.from(document.querySelectorAll('input[name="getting[]"]')).map(input => input.value.trim()).filter(Boolean);

        if (givingPlayers.length === 0 || gettingPlayers.length === 0) {
            resultText.textContent = "You must add at least one player in both 'Giving' and 'Getting' sections.";
            resultContainer.style.display = 'block';
            return;
        }

        const formData = new URLSearchParams();
        givingPlayers.forEach(player => formData.append('giving[]', player));
        gettingPlayers.forEach(player => formData.append('getting[]', player));

        fetch('/compare/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': csrfToken,
            },
            body: formData.toString(),
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
