"use strict";

var json = "{\"name\": \"Oria\", \"health\": 6, \"stats\": {\"strength\": 1, \"dexterity\": 1, \"constitution\": 2, \"intelligence\": 3, \"wisdom\": 1, \"charisma\": 2}, \"traits\": {\"Body\": \"\u0413\u0440\u043E\u043C\u0430\u0434\u043D\u043E\u0435\", \"Face\": \"\u0415\u0445\u0438\u0434\u043D\u043E\u0435\", \"Clothing\": \"\u041F\u043E\u0442\u0451\u0440\u0442\u0430\u044F\", \"Skin\": \"\u0417\u043B\u043E\u0432\u043E\u043D\u043D\u0430\u044F\", \"Virtue\": \"\u0426\u0435\u043B\u0435\u0443\u0441\u0442\u0440\u0435\u043C\u043B\u0451\u043D\u043D\u043E\u0441\u0442\u044C\", \"Hair\": \"\u041B\u043E\u043C\u043A\u0438\u0435\", \"Vice\": \"\u0410\u0433\u0440\u0435\u0441\u0441\u0438\u0432\u043D\u043E\u0441\u0442\u044C\", \"Speech\": \"\u0417\u0430\u0438\u043A\u0430\u044E\u0449\u0430\u044F\u0441\u044F\", \"Background\": \"\u041A\u043E\u043D\u0442\u0440\u0430\u0431\u0430\u043D\u0434\u0438\u0441\u0442\", \"Misfortune\": \"\u0417\u0430\u043C\u0435\u043D\u0451\u043D\"}}";
var DATA = JSON.parse(json); // const url = 'http://127.0.0.1:8000/knave/create_character/';
// let xhr = new XMLHttpRequest();
// xhr.open('GET', url, false);
// xhr.send();
// let DATA = JSON.parse(xhr.responseText);

var nameOutput = document.querySelector('.name-container__output');
var button = document.querySelector('.button');
var healthOutput = document.querySelector('.armor-container__max-output');

button.onclick = function (element) {
  element.preventDefault();
  nameOutput.textContent = DATA.name;
  healthOutput.textContent = DATA.health;

  for (key in DATA.stats) {
    document.querySelector('.' + key + '-container__bonus-output').textContent = DATA.stats[key];
  }

  for (key in DATA.traits) {
    document.querySelector('.' + key.toLowerCase() + '-container__trait-output').textContent = DATA.traits[key];
  }
}; // write api request
// code rendering of defense stats (armor_class = armor defense, armor bonus = armor defense - 10, defense = bonus + 10)
// make sheet cells render on window load
// find out how to make api call from my server (install python latest, pip install, requirements.txt, runserver)
// find out what button do by default