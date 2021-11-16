"use strict";

// choose all insert elements
// write for i algho to sort data in them
// write api request
var url = '';
var xhr = new XMLHttpRequest();
xhr.open('GET', url, false);
xhr.send();
var DATA = JSON.parse(xhr.responseText);
bonusOutputCells = document.querySelectorAll('p[class$="bonus-output"]');
DATA.forEach(function (ability) {});