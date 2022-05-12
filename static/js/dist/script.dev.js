"use strict";

// let json = '{"name": "Oria", "health": 6, "stats": {"strength": 1, "dexterity": 1, "constitution": 2, "intelligence": 3, "wisdom": 1, "charisma": 2}, "traits": {"Body": "\u0413\u0440\u043e\u043c\u0430\u0434\u043d\u043e\u0435", "Face": "\u0415\u0445\u0438\u0434\u043d\u043e\u0435", "Clothing": "\u041f\u043e\u0442\u0451\u0440\u0442\u0430\u044f", "Skin": "\u0417\u043b\u043e\u0432\u043e\u043d\u043d\u0430\u044f", "Virtue": "\u0426\u0435\u043b\u0435\u0443\u0441\u0442\u0440\u0435\u043c\u043b\u0451\u043d\u043d\u043e\u0441\u0442\u044c", "Hair": "\u041b\u043e\u043c\u043a\u0438\u0435", "Vice": "\u0410\u0433\u0440\u0435\u0441\u0441\u0438\u0432\u043d\u043e\u0441\u0442\u044c", "Speech": "\u0417\u0430\u0438\u043a\u0430\u044e\u0449\u0430\u044f\u0441\u044f", "Background": "\u041a\u043e\u043d\u0442\u0440\u0430\u0431\u0430\u043d\u0434\u0438\u0441\u0442", "Misfortune": "\u0417\u0430\u043c\u0435\u043d\u0451\u043d"}}';
// let DATA = JSON.parse(json);
// const url = 'http://127.0.0.1:8000/knave/create_character/';
var url = 'https://api.kanye.rest/';

function getStats(event) {
  event.preventDefault();
  fetch(url).then(function (response) {
    return response.json();
  }).then(function (data) {
    nameOutput.textContent = data.quote;
    healthOutput.textContent = data.quote;
  });
}

var nameOutput = document.querySelector('.name-container__output');
var button = document.querySelector('.button');
var healthOutput = document.querySelector('.armor-container__max-output');
button.addEventListener("click", getStats); // button.onclick = function(element) {
//     element.preventDefault();
//     nameOutput.textContent = data.name; 
//     healthOutput.textContent = data.health;
//     for (key in data.stats) {
//         document.querySelector('.'+ key +'-container__bonus-output').textContent = data.stats[key];
//     }
//     for (key in DATA.traits) {
//         document.querySelector('.' + key.toLowerCase() + '-container__trait-output').textContent = data.traits[key];
//     }
// }
// Update api request to new api structure
// code rendering of defense stats (armor_class = armor defense, armor bonus = armor defense - 10, defense = bonus + 10)
// make sheet cells render on window load