from django.db import models


# TODO модели персонажей
# TODO Модели предметов
# TODO Модели трейтов


class Trait(models.Model):
    type = models.CharField(max_length=50)
    trait_title = models.CharField(max_length=75)


class Name(models.Model):
    name = models.CharField(max_length=50)


class Item(models.Model):
    item_title = models.CharField(max_length=100, unique=True)
    quantity = models.SmallIntegerField(blank=True)
    dimension = models.CharField(max_length=30, blank=True)


