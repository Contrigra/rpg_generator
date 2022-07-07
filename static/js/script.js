const url = 'http://84.201.140.229/knave/character/generate';

const dataForTest = {"name": "Francis", "health": 4, "stats": {"strength": 2, "dexterity": 3, "constitution": 4, "intelligence": 6, "wisdom": 2, "charisma": 1}, "traits": {"body": "\u0422\u0443\u0447\u043d\u043e\u0435", "face": "\u041a\u0432\u0430\u0434\u0440\u0430\u0442\u043d\u043e\u0435", "clothing": "\u042d\u043a\u0441\u0446\u0435\u043d\u0442\u0440\u0438\u0447\u043d\u0430\u044f", "skin": "\u0411\u043e\u0435\u0432\u0430\u044f \u0440\u0430\u0441\u043a\u0440\u0430\u0441\u043a\u0430", "virtue": "\u0422\u0435\u0440\u043f\u0438\u043c\u043e\u0441\u0442\u044c", "hair": "\u0412\u043e\u043b\u043d\u0438\u0441\u0442\u044b\u0435", "vice": "\u0410\u0433\u0440\u0435\u0441\u0441\u0438\u0432\u043d\u043e\u0441\u0442\u044c", "speech": "\u0417\u0430\u0433\u0430\u0434\u043e\u0447\u043d\u0430\u044f", "background": "\u041a\u0430\u0440\u043c\u0430\u043d\u043d\u0438\u043a", "misfortune": "\u0418\u0437\u0433\u043d\u0430\u043d"}, "inventory": [["\u0421\u043f\u0438\u0447\u043a\u0438", ["\u0421\u0432\u0435\u0447\u0438", 5]], ["\u0401\u0436\u0438\u043a\u0438"], ["\u0413\u0443\u0431\u043a\u0430"]], "armor": {"body": ["\u0421\u0442\u0451\u0433\u0430\u043d\u0430\u044f", 12], "auxiliary_items": ["\u0428\u043b\u0435\u043c \u0438 \u0449\u0438\u0442", 2], "armor_class": 14}};

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
    armorBonusOutput.textContent = content.armor.armor_class - 10;
    armorDefenseOutput.textContent = content.armor.armor_class;
}

// function getData(event) {
//     event.preventDefault();
//     fetch(url)
//     .then((response) => {
//         if (!response.ok) {
//             console.log('Network response was not OK');
//         }
//         return response.json();
//     })
//     .then(data => insertContent(data))
//     .catch(error => console.error('There has been a problem with your fetch operation:', error))
// }

function testInsertContent() {
    insertContent(dataForTest);
}

window.addEventListener('load', testInsertContent);
button.addEventListener('click', testInsertContent);


