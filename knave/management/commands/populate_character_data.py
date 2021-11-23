from knave.models import Name, Trait
from django.core.management.base import BaseCommand, CommandError


traits = {'Body':
              ['Атлетичное', 'Мускулистое', 'Тучное', 'Изящное', 'Костлявое',
               'Громадное',
               'Долговязое', 'Накачанное', 'Грубое', 'Худое', 'Короткое',
               'Жилистое',
               'Стройное', 'Дряблое', 'Статное', 'Коренастое', 'Миниатюрное',
               'Великанье',
               'Гибкое', 'Закалённое', ],
          'Face':
              ['Раздутое', 'Грубое', 'Костлявое', 'Точечное', 'Утончённое',
               'Продолговатое',
               'Королевское', 'Сжатое', 'Ястребиное', 'Повреждённое',
               'Ехидное',
               'Узкое',
               'Крысиное', 'Круглое', 'Впалое', 'Острое', 'Мягкое',
               'Квадратное',
               'Широкое',
               'Волчье'],
          'Clothing':
              ['Старинная', 'Окровавленная', 'Церемониальная', 'Украшенная',
               'Эксцентричная', 'Элегантная', 'Модная', 'Грязная',
               'Вызывающая',
               'Запачканная', 'Иноземная', 'Потёртая', 'Старомодная',
               'Униформа',
               'Мешковатая', 'Взаплатках', 'Надушенная', 'Мерзкая',
               'Порванная',
               'Малорослая'],
          'Skin':
              ['Боевой шрам', 'Родимое пятно', 'Ожог', 'Тёмная', 'Макияж',
               'Жирная',
               'Бледная', 'Идеальная', 'Пирсинг', 'Рябая', 'Зловонная',
               'Татуировки',
               'Благоухающая', 'Грубая', 'Обвисшая', 'Солнечный ожог',
               'Загорелая',
               'Боевая раскраска', 'Дряблая', 'Шрамы от кнута', ],
          'Virtue':
              ['Амбициозность', 'Осторожность', 'Храбрость', 'Обходительность',
               'Любознательность', 'Дисциплинированность',
               'Целеустремлённость',
               'Щедрость',
               'Общительность', 'Честность', 'Великодушие', 'Скромность',
               'Идеализм',
               'Простота', 'Лояльность', 'Милосердие', 'Праведность',
               'Невозмутимость',
               'Стойкость', 'Терпимость', ],
          'Hair':
              ['Лысина', 'Косы', 'Короткострижены', 'Грубообрезаны',
               'Кудрявые',
               'Взлохмачены', 'Дреды', 'Грязные', 'Вьющиеся', 'Сальные',
               'Ломкие',
               'Длинные', 'Шикарные', 'Ирокез', 'Блестящие', 'Хвост',
               'Шелковистые',
               'Узел',
               'Волнистые', 'Тонкие', ],
          'Vice':
              ['Агрессивность', 'Надменность', 'Обидчивость',
               'Трусость', 'Жестокость',
               'Лживость', 'Легкомысленность', 'Обжорство', 'Жадность',
               'Раздражительность',
               'Лень', 'Нервозность', 'Предубеждения', 'Безрассудство',
               'Грубость',
               'Подозрительность', 'Тщеславие', 'Мстительность',
               'Расточительность',
               'Нытьё', ],
          'Speech':
              ['Грубая', 'Громогласная', 'Задыхающаяся', 'Загадочная',
               'Проглатывающая',
               'Слюнявая', 'Высокопарная', 'Официозная', 'Загробная',
               'Хриплая',
               'Бормочущая', 'Краткая', 'Причудливая', 'Бессвязная',
               'Скороговорная',
               'Акцент', 'Медленная', 'Пищащая', 'Заикающаяся', 'Шепчущая',
               ],
          'Background':
              ['Алхимик', 'Попрошайка', 'Мясник', 'Грабитель', 'Шарлатан',
               'Священник',
               'Повар', 'Культист', 'Картёжник', 'Травник', 'Волшебник',
               'Моряк', 'Наёмник',
               'Торговец', 'Бандит', 'Актёр', 'Карманник', 'Контрабандист',
               'Студент',
               'Охотник', ],
          'Misfortune':
              ['Сирота', 'Зависим', 'Шантажируется', 'Осуждён', 'Проклят',
               'Обманут',
               'Расжалован', 'Дискредитирован', 'Отрёкся', 'Изгнан',
               'Подставлен',
               'Одержим', 'Похищен', 'Изувечен', 'Банкрот', 'Преследуемый',
               'Отвергнут',
               'Заменён', 'Ограблен', 'Подозреваемый']}



class Command(BaseCommand):
    help = 'Populates DB with starting data'

    def handle(self, *args, **options):
        with open('knave/management/commands/names.txt', 'r',
                  encoding='utf8') as f:
            names_list_dirty = f.readlines()
            for item in names_list_dirty:
                item = item.strip('\n')
                Name.objects.get_or_create(name=item)

    for keys, values in traits.items():
        print(f'\n{keys}')
        for item in values:
            trait = Trait.objects.get_or_create(title=item)
            trait[0].tags.add(f'{keys}')

    # TODO ? Loading items?