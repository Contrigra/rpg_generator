from .knave_character import generate_knave_character


def get_knave_character_as_string():
    pc = generate_knave_character()  # player character

    pc_auxiliary_items = ''
    if None not in pc.armor['auxiliary_items']:
        pc_auxiliary_items = f"{pc.armor['auxiliary_items']}"

    pc_string = f'''
    Тебя зовут - {pc.name} 
    HP - {pc.health}

    Сила - {pc.stats['strength']}     
    Ловкость - {pc.stats['dexterity']} 
    Телосложение - {pc.stats['constitution']}
    Интеллект - {pc.stats['intelligence']}
    Мудрость - {pc.stats['wisdom']}
    Харизма - {pc.stats['charisma']}

    Броня - {pc.armor['armor_class']}
    Предметы брони: {pc.armor['body']} {pc_auxiliary_items}

    Инвентарь: {pc.inventory}

    Особенности:
    Тело - {pc.traits['body']}
    Лицо - {pc.traits['face']}
    Одежда - {pc.traits['clothing']}
    Кожа - {pc.traits['skin']}
    Волосы - {pc.traits['hair']}
    Порок - {pc.traits['vice']}
    Добродетель - {pc.traits['virtue']}
    Речь  - {pc.traits['speech']}
    Прошлое - {pc.traits['background']}
    Неудача - {pc.traits['misfortune']}
    '''

    return pc_string
