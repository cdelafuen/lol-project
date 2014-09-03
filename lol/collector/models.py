# -*- coding: utf-8 -*-
import json
from django.db import models
import requests


class FightingType(models.Model):
    type = models.CharField(max_length=45, primary_key=True)

    def __unicode__(self):
        return self.type


class Champion(models.Model):
    champion_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    attack = models.PositiveSmallIntegerField()
    magic = models.PositiveSmallIntegerField()
    defense = models.PositiveSmallIntegerField()
    difficulty = models.PositiveSmallIntegerField()
    sex = models.CharField(max_length=45)
    partype = models.CharField(max_length=45)
    fighting_types = models.ManyToManyField(FightingType, through='ChampionFightingType', blank=True, null=True)

    def __unicode__(self):
        return self.name


class ChampionFightingType(models.Model):
    champion = models.ForeignKey(Champion)
    fighting_type = models.ForeignKey(FightingType)


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


def update_champions():
    # request
    response = requests.get("http://ddragon.leagueoflegends.com/cdn/4.4.3/data/es_ES/champion.json")
    if response.status_code == 200:
        champions = json.loads(response.content)
        for champion in champions['data']:
            basic_params = champions['data'][champion]['info']
            c, created = Champion.objects.get_or_create(champion_id=champions['data'][champion]['key'],
                                                        name=champions['data'][champion]['name'],
                                                        attack=basic_params['attack'], defense=basic_params['defense'],
                                                        magic=basic_params['magic'], difficulty=basic_params['difficulty'],
                                                        partype=champions['data'][champion]['partype'])
            tags = champions['data'][champion]['tags']
            for type in tags:
                ft, created = FightingType.objects.get_or_create(type=type)
                ChampionFightingType.objects.get_or_create(champion=c, fighting_type=ft)
                print c, type, ft, created