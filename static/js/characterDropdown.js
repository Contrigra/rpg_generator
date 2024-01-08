export default function createCharacterDropdown() {
    const dropdownDivButton = document.createElement('div');
    dropdownDivButton.classList.add('character-dropdown-button');
    dropdownDivButton.textContent = 'Персонажи';
    const controlPanel = document.querySelector('.character-control-container');
    controlPanel.appendChild(dropdownDivButton);


    const dropdownItemContainer = document.createElement('div');
    dropdownItemContainer.classList.add('dropdown-reveal-container');
    dropdownDivButton.appendChild(dropdownItemContainer);

    dropdownDivButton.addEventListener('click', () => {
        clearDropdown();
        expandDropdown();
    });
}

function expandDropdown() {
    const dropdownItemContainer = document.querySelector('.dropdown-reveal-container');
    // TODO добавить нижний марджин кнопке дропдайнуа
    for (const data of JSON.parse(localStorage.getItem('characterArray'))) {
        dropdownItemContainer.appendChild(createDropdownItem(data.name, data.health));
    }
}

// TODO функция которая убрает дропдаун
function clearDropdown() {
    const dropdownDiv = document.createElement('div');
}

function createDropdownItem(name, hp) {
    const characterDiv = document.createElement('div');
    characterDiv.classList.add('character-div-item');
    characterDiv.textContent = `${name}, ${hp}`;
    return characterDiv;
}