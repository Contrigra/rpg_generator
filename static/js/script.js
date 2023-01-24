const url = `${location.protocol}//${location.host}/knave/character/generate/`;

const button = document.querySelector('.button');
const nameOutput = document.querySelector('.name-container__output');
const healthOutput = document.querySelector('.hit-points-container__max-output');
const armorBonusOutput = document.querySelector('.armor-container__bonus-output');
const armorDefenseOutput = document.querySelector('.armor-container__defense-output');


function insertContent(content) {
    nameOutput.textContent = content.name;
    healthOutput.textContent = content.health;
    for (key in content.stats) {
        document.querySelector('.' + key + '-container__bonus-output').textContent = content.stats[key];
        document.querySelector('.' + key.toLowerCase() + '-container__defense-output').textContent = content.stats[key] + 10;
    }
    for (key in content.traits) {
        document.querySelector('.' + key.toLowerCase() + '-container__trait-output').textContent = content.traits[key];
    }

    // TODO сделать рендер двух частей инвентаря. Броня, если есть, и прочие предметы



    armorBonusOutput.textContent = content.armor.armor_class - 10;
    armorDefenseOutput.textContent = content.armor.armor_class;
}

// TODO инвентарь - броня, другие предметы
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

window.addEventListener('load', getData);
button.addEventListener('click', getData);


