const url = 'https://api.kanye.rest/';

// const url = 'http://127.0.0.1:8000/knave/create_character/';

const nameOutput = document.querySelector('.name-container__output');
const button = document.querySelector('.button');
const healthOutput = document.querySelector('.armor-container__max-output');

function insertContent(content) {
    nameOutput.textContent = content.name; 
    healthOutput.textContent = content.health;
    for (key in content.stats) {
        document.querySelector('.'+ key +'-container__bonus-output').textContent = content.stats[key];
    }
    for (key in content.traits) {
        document.querySelector('.' + key.toLowerCase() + '-container__trait-output').textContent = content.traits[key];
    }
}

function getData(event) {
    event.preventDefault();
    fetch(url)
    .then((response) => {
        if (!response.ok) {
            console.log('Network response was not OK');
        }
        return response.json();
    })
    .then(data => insertContent(data))
    .catch(error => console.error('There has been a problem with your fetch operation:', error))
}

button.addEventListener("click", getData);




// Update insertContent() up to new src structure
// Make sheet cells render on window load

