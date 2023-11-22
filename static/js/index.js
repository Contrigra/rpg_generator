import contentRender from "./renderContent.js";


localStorage.setItem('characterArray', '[]');

const button = document.querySelector('.button');
// const characterArray =
window.addEventListener('load', e => getData(e));
button.addEventListener('click', e => getData(e));


function getData(event) {
    const url = `${location.protocol}//${location.host}/knave/character/generate/`;

    event.preventDefault();
    fetch(url)
        .then((response) => {
            if (!response.ok) {
                console.log('Network response was not OK');
            }
            return response.json();
        })
        .then(data => saveData(data))
        .then(data => contentRender(data))
        .catch(error => console.error('There has been a problem with your fetch operation:', error))
}

function saveData(data) {
    const characterArray = JSON.parse(localStorage.getItem('characterArray'));
    // store no more than 10 last characters
    if (characterArray.length === 10) {
        characterArray.shift()
    }
    characterArray.push(data);
    localStorage.setItem('characterArray', JSON.stringify(characterArray));
    return data
}

function createDropDown() {

}