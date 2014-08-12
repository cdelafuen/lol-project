# -*- coding: utf-8 -*-
import json
from django.db import models
import requests


# Create your models here.
class Champion(models.Model):

    champion_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    sex = models.CharField(max_length=45, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Summoner(models.Model):
    summoner_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    profile_icon_id = models.IntegerField()
    revision_date = models.DateTimeField()
    level = models.PositiveSmallIntegerField()


class Api(models.Model):
    BR = 'br'
    EUNE = 'eune'
    EUW = 'euw'
    KR = 'kr'
    LAN = 'lan'
    LAS = 'las'
    NA = 'na'
    OCE = 'oce'
    RU = 'ru'
    TR = 'tr'
    SERVER_CHOICES = {
        (BR, 'br'),
        (EUNE, 'eune'),
        (EUW, 'euw'),
        (KR, 'kr'),
        (LAN, 'lan'),
        (LAS, 'las'),
        (NA, 'na'),
        (OCE, 'oce'),
        (RU, 'ru'),
        (TR, 'tr'),
    }

    version = models.CharField(max_length=5)
    server = models.CharField(max_length=5, choices=SERVER_CHOICES, default=EUW)


def update_champions(self):
    # request
    response = requests.get("http://ddragon.leagueoflegends.com/cdn/4.4.3/data/es_ES/champion.json")
    if response.status_code == 200:
        champions = json.loads(response.content)
        for champion in champions['data']:
            print champions['data'][champion]
            Champion.objects.get_or_create(champion_id=champions['data'][champion]['key'],
                                           name=champions['data'][champion]['name'])