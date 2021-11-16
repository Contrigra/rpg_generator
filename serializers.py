from rest_framework import serializers
from django.db import models
from rest_framework.fields import DictField, CharField


class CharacterSerializer(serializers.Serializer):
    name = CharField(max_length=50)
    stats = DictField()

    #TODO other fields
