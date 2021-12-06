from rest_framework import serializers
from django.db import models
from rest_framework.fields import DictField, CharField, IntegerField, ListField


class CharacterSerializer(serializers.Serializer):
    name = CharField(max_length=50)
    health = IntegerField()
    stats = DictField()
    traits = DictField()
    inventory = ListField()
    armor = DictField()
