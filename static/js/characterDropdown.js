import contentRender from "./renderContent.js";

export default function createCharacterDropdown() {
    const dropdownDivButton = document.createElement('div');
    dropdownDivButton.classList.add('character-dropdown-button');
    dropdownDivButton.textContent = 'Персонажи';

    const controlPanel = document.querySelector('.character-control-container');
    controlPanel.appendChild(dropdownDivButton);

    const dropdownItemContainer = document.createElement('div');
    dropdownItemContainer.classList.add('dropdown-reveal-container');
    dropdownDivButton.appendChild(dropdownItemContainer);
    // avoid firing the event on children of the button
    dropdownDivButton.addEventListener('click', (e) => {
        if (e.target.className !== 'character-dropdown-button') return;
        toggleDropdown();
    });
}

export function toggleDropdown() {
    const dropdownItemContainer = document.querySelector('.dropdown-reveal-container');
    if (dropdownItemContainer.classList.contains('revealed')) {
        clearDropdown();
    } else {
        clearDropdown();
        expandDropdown();
    }
    dropdownItemContainer.classList.toggle('revealed')
}

function expandDropdown() {
    const dropdownItemContainer = document.querySelector('.dropdown-reveal-container');
    for (const [index, data] of JSON.parse(localStorage.getItem('characterArray')).entries()) {
        dropdownItemContainer.appendChild(createDropdownItem(index, data));
    }
}

function clearDropdown() {
    const dropdownItemContainer = document.querySelector('.dropdown-reveal-container')
    dropdownItemContainer.replaceChildren()
}

function createDropdownItem(index, data) {
    const characterDiv = document.createElement('div');
    characterDiv.classList.add('character-div-item');
    characterDiv.classList.add(`${index}`)
    characterDiv.textContent = `${data.name}, ${data.health}`;

    characterDiv.addEventListener('click', () => {
        pickCharacter(data)
    })
    return characterDiv;
}

function pickCharacter(data) {
    toggleDropdown()
    contentRender(data)
}
