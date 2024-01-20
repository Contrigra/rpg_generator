import contentRender from "./renderContent.js";
import createCharacterDropdown, {toggleDropdown} from "./characterDropdown.js";
import CharacterDataController from "./characterData.js";

const characterData = new CharacterDataController();
const button = document.querySelector('.button');
button.addEventListener('click', e => {
    const dropdownItemContainer = document.querySelector('.dropdown-reveal-container');
    // hide dropdown if it's revealed on new character button press.
    if (dropdownItemContainer.classList.contains('revealed')) {
        toggleDropdown()
    }
    getData(e)
});
window.addEventListener('load', e => getData(e));

createCharacterDropdown();

function getData(event) {
    const url = `${location.protocol}//127.0.0.1:8000/knave/character/generate/`;
    event.preventDefault();
    fetch(url)
        .then((response) => {
            if (!response.ok) {
                console.log('Network response was not OK');
            }
            return response.json();
        })
        .then(data => characterData.saveCharacter(data))
        .then(data => contentRender(data))
        .catch(error => console.error('There has been a problem with your fetch operation:', error))
}

