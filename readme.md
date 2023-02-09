# RPG_Generator

## Current Website URL

https://rpgenerator.ru/

## About the project

This is a simple character generator for Knave TTRPG. Currently, works only in
Russian language

## How does it work?

Whenever you open the page, you automatically obtain a newly generated
character. If you want to generate a new character, press the only button on
page

## Reason for the project?

Knave is a really deadly game, and my players were gloom, if death was bitter.
So this was my way of soothing the pain.

Additionally, Knave is a wonderful TTRPG, so I hope it may help other people to
get on board or get inured to OSR deadliness :)

# First time start

### Make initial django migrations

> python manage.py makemigrations && python manage.py migrate

### After that, you may populate the default database (sqlite) with provided data in Russian

> python manage.py populate_character_data

Data is stored in plain .txt file

### Create a new superuser

> python manage.py createsuperuser

### vkbot app

Vkbot app provides an easy way to make your own VK bot. Just provide needed
variables in your .env file:

- VK_SECRET
- VK_ACCESS_TOKEN
- VK_GROUP_ID
- VK_API_VERSION 

After that you may customize or use it as you wish

## TODO

Project is completed for current needs, but I may add further functionality as
needed or interested.

What I think I could implement:

- Proper Naming
- Generators for other games and needs
- Telegram and discord bot

## Notes

- My project uses nginx to serve static files, so set up a server of your
  choice

- Knave TTRPG by [Questing Beast](http://questingblog.com/knave/) Under Commons
  Attribution 4.0 International License
