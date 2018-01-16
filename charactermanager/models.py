import datetime

from django.db import models
from django.utils import timezone

class Player(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Character(models.Model):

    BARBARIAN = 'BN'
    BARD = 'BD'
    CLERIC = 'CC'
    DRUID = 'DD'
    FIGHTER = 'FR'
    MONK = 'MK'
    PALADIN = 'PN'
    RANGER = 'RR'
    ROGUE = 'RE'
    SORCERER = 'SR'
    WARLOCK = 'WK'
    WIZARD = 'WD'
    CHARACTER_CLASS_CHOICES = (
        (BARBARIAN, 'Barbarian'),
        (BARD, 'Bard'),
        (CLERIC, 'Cleric'),
        (DRUID, 'Druid'),
        (FIGHTER, 'Fighter'),
        (MONK, 'Monk'),
        (PALADIN, 'Paladin'),
        (RANGER, 'Ranger'),
        (ROGUE, 'Rogue'),
        (SORCERER, 'Sorcerer'),
        (WARLOCK, 'Warlock'),
        (WIZARD, 'Wizard'),
    )
    character_class = models.CharField(
        max_length=2,
        choices=CHARACTER_CLASS_CHOICES,
        default=FIGHTER,
    )

    level = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    sub_class = models.CharField(max_length=200)
    race = models.CharField(max_length=200)
    is_alive = models.BooleanField(default=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    def __str__(self):
        return self.name
