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
adresse=Adresse("Marseille","France")
adresse.afficher()
entreprise=Entreprise("Entreprise test",adresse,16.5)
entreprise.afficher()
ecurie=Ecurie("Audi",adresse,17.5)
ecurie.searchVoiture(int(0))
voiture=Voiture(0,"Berline",12,12000,402)
voiture.afficher()
pilote=Pilote("Sheev Palpatine","Dark Sidious",382,Statut.CO_PILOTE,voiture,Saison.AUTONOMNE)
pilote.afficher()
copilote=Pilote("Skylwalker","Anakin",67,Statut.PILOTE,voiture,Saison.AUTONOMNE)
copilote.afficher()
contrat=Contrat(Saison.HIVER,ecurie,pilote,copilote)
contrat.afficher()
with open('listeVoiture.json', 'r') as f:
    datas = json.load(f)
    pprint(datas["tabVoiture"][0])
print(type(datas))
