import contentRender from "./renderContent.js";

export default class CharacterDataController {
    constructor() {
        localStorage.setItem('characterArray', '[]');
    }


    saveCharacter(data) {
        // Using array as a queue to store no more than 10 characters
        this.characterArray = JSON.parse(localStorage.getItem('characterArray'));
        if (this.characterArray.length === 10) {
            this.characterArray.shift()
        }
        this.characterArray.push(data);
        this.currentCharacter = data;
        localStorage.setItem('characterArray', JSON.stringify(this.characterArray));
        return data
    }

    // for future use
    switchCharacter(data) {
        this.currentCharacter = data
        contentRender(data)
    }
}
