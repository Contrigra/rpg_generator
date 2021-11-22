// choose all insert elements
// write for i algho to sort data in them
// write api request

let DATA = {
    name: "Tybalt", 
    stats: {
        strength: 4, 
        dexterity: 3, 
        constitution: 2, 
        intelligence: 4, 
        wisdom: 1, 
        charisma: 1
    }
};

// const url = '';

// let xhr = new XMLHttpRequest();
// xhr.open('GET', url, false);
// xhr.send();
// let DATA = JSON.parse(xhr.responseText);

const bonusOutputCells = document.querySelectorAll('p[class$="bonus-output"]');

const nameOutput = document.querySelector('.name-container__output');

nameOutput.textContent = DATA.name; 

console.log(DATA.stats.charisma);