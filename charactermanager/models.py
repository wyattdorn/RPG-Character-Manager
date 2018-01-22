import datetime

from django.db import models
from django.utils import timezone

class Player(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Vampire(models.Model):
    BRUJAH = 'BH'
    GANGREL = 'GL'
    MALKAVIAN = 'MN'
    NOSFERATU = 'NU'
    TOREADOR = 'TR'
    TREMERE = 'TE'
    VENTRUE = 'VE'
    CAITIFF = 'CF'
    CLAN_CHOICES = (
        (BRUJAH, 'Brujah'),
        (GANGREL, 'Gangrel'),
        (MALKAVIAN, 'Malkavian'),
        (NOSFERATU, 'Nosferatu'),
        (TOREADOR, 'Toreador'),
        (TREMERE, 'Tremere'),
        (VENTRUE, 'Ventrue'),
        (CAITIFF, 'Caitiff'),
    )
    vampire_clan = models.CharField(
        max_length=2,
        choices=CLAN_CHOICES,
        default=CAITIFF,
    )

    ANARCH = 'AH'
    CAMARILLA = 'CA'
    SABBAT = 'ST'
    SECT_CHOICES = (
        (ANARCH, 'Anarch'),
        (CAMARILLA, 'Camarilla'),
        (SABBAT, 'Sabat'),
    )
    sect = models.CharField(
        max_length=2,
        choices=SECT_CHOICES,
        default=CAMARILLA,
    )

    name = models.CharField(max_length=200)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    #sire = models.ForeignKey(Vampire, on_delete=models.CASCADE, default=None)
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
