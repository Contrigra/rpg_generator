// choose all insert elements
// write for i algho to sort data in them
// write api request

const url = '';

let xhr = new XMLHttpRequest();
xhr.open('GET', url, false);
xhr.send();
let DATA = JSON.parse(xhr.responseText);

bonusOutputCells = document.querySelectorAll('p[class$="bonus-output"]');

DATA.forEach(ability => {

});