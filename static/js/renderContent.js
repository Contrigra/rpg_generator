export default function contentRender(data) {
    const {inventory, stats, armor, name, health, traits} = data;

    nameRender(name);
    healthRender(health);
    bonusDefenseRender(stats);
    traitRender(traits);
    armorStatRender(armor);
    armorItemRender(armor, inventory);

}


function nameRender(name) {
    const nameOutput = document.querySelector('.name-container__output');
    nameOutput.textContent = name;
}

function healthRender(health) {
    const healthOutput = document.querySelector('.hit-points-container__max-output');
    healthOutput.textContent = health;

}

function armorItemRender(armor, inventory) {
    const inventoryOutput = document.querySelector('.items-container__item-output');
    const armorItemsOutput = document.querySelector('.armor-container__item-output');

    armorItemsOutput.textContent = '' // if I did not clear the content, it would save previous result and get stacked
    armorItemsOutput.insertAdjacentHTML("afterbegin", `<ul>${armor.body}</ul>`);
    if (armor.auxiliary_items[0] !== null) {
        armorItemsOutput.insertAdjacentHTML("afterbegin", `<ul>${armor.auxiliary_items}</ul>`);
    }
    inventoryOutput.textContent = ''
    for (let i = 0; i < inventory.length; i++) {
        inventoryOutput.insertAdjacentHTML("afterbegin", `<ul>${inventory[i]}</ul>`);
    }

}

function bonusDefenseRender(stats) {
    for (let key in stats) {
        document.querySelector('.' + key + '-container__bonus-output').textContent = stats[key];
        document.querySelector('.' + key.toLowerCase() + '-container__defense-output').textContent = stats[key] + 10;
    }
}

function armorStatRender(armor) {
    const armorBonusOutput = document.querySelector('.armor-container__bonus-output');
    const armorDefenseOutput = document.querySelector('.armor-container__defense-output');

    armorBonusOutput.textContent = armor.armor_class - 10;
    armorDefenseOutput.textContent = armor.armor_class;
}

function traitRender(traits) {
    for (let key in traits) {
        document.querySelector('.' + key.toLowerCase() + '-container__trait-output').textContent = traits[key];
    }
}