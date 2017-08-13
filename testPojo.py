#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  testPojo.py
#  
#  Copyright 2017 BlackAllSun <attilavlh10@gmail.com>
#  
#  
from pprint import pprint
import json
from pojo import *
builder=BuilderJSON()
adresse=Adresse(0,"Marseille","France")
adresse.afficher()
entreprise=Entreprise(0,"Entreprise test",adresse,16.5)
entreprise.afficher()
ecurie=Ecurie(1,"Audi",adresse,17.5)
builder.searchVoiture(int(0))
voiture=Voiture(0,"Berline",12,12000,402)
voiture.afficher()
pilote=Pilote(0,"Sheev Palpatine","Dark Sidious",382,Statut.CO_PILOTE,voiture)
pilote.afficher()
copilote=Pilote(1,"Skylwalker","Anakin",67,Statut.PILOTE,voiture)
copilote.afficher()
adresseSponsor=Adresse(1,"Marseille","France")
adresseSponsor.afficher()
sponsor=Sponsor(2,"JePayeDesCourses",adresseSponsor,14000)
contrat=Contrat(0,Saison.HIVER,ecurie,pilote,copilote,sponsor,voiture)
contrat.afficher()
builder.searchContrat(int(0))
with open('listeVoiture.json', 'r') as f:
    datas = json.load(f)
    pprint(datas["tabVoiture"][0])
print(type(datas))
