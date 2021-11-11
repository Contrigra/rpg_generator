from django.db import models
from taggit.managers import TaggableManager


class Trait(models.Model):
    """A model for Character Traits"""
    tags = TaggableManager()
    title = models.CharField(max_length=75)


class Name(models.Model):
    """Simple Character name model"""
    name = models.CharField(max_length=50)


class Item(models.Model):
    """Model of possible items, items can be countable and measurable"""
    item_title = models.CharField(max_length=100, unique=True)
    quantity = models.SmallIntegerField(blank=True)
    dimension = models.CharField(max_length=30, blank=True)
