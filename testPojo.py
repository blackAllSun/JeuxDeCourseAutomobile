#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  testPojo.py
#  

from pprint import pprint
import json
from pojo import *
from Adresse import *
from Contrat import *
from Ecurie import *
from Entreprise import *
from Pilote import *
from Sponsor import *
from Voiture import *
builder=BuilderJSON()
adresse=Adresse(0,"Marseille","France")
print(adresse)
entreprise=Entreprise(0,"Entreprise test",adresse,16.5)
print(entreprise)
ecurie=Ecurie(1,"Audi",adresse,17.5)
builder.searchVoiture(int(0))
voiture=Voiture(0,"Berline",12,12000,402)
print(voiture)
pilote=Pilote(0,"Sheev Palpatine","Dark Sidious",382,Statut.CO_PILOTE,voiture)
print(pilote)
copilote=Pilote(1,"Skylwalker","Anakin",67,Statut.PILOTE,voiture)
print(copilote)
adresseSponsor=Adresse(1,"Marseille","France")
print(adresseSponsor)
sponsor=Sponsor(2,"JePayeDesCourses",adresseSponsor,14000)
contrat=Contrat(0,Saison.HIVER,ecurie,pilote,copilote,sponsor,voiture)
print(contrat)
builder.searchContrat(int(0))
with open('listeVoiture.json', 'r') as f:
    datas = json.load(f)
    pprint(datas["tabVoiture"][0])
print(type(datas))
