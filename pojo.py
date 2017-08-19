#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pojo.py
#  
from pprint import pprint
import json
from pojo import *
from numpy import array
import numpy as np
from enum import Enum 
class BuilderJSON(object):
	def __init__(self):
		print("builder")
	def searchAdresse(self,idAdresse):
		with open('listeVoiture.json', 'r') as f:
			datas = json.load(f)
			idAdresse=int(datas["tabAdresse"][idAdresse]["idAdresse"])
			ville=datas["tabAdresse"][idAdresse]["ville"]
			pays=datas["tabAdresse"][idAdresse]["pays"]
			adresse=Adresse(idAdresse,ville,pays)
		return adresse
	def searchVoiture(self,idVoit):
		with open('listeVoiture.json', 'r') as f:
			datas = json.load(f)
			idVoiture=int(datas["tabVoiture"][idVoit]["idVoit"])
			print(type(idVoiture))
			modele=datas["tabVoiture"][idVoit]["modele"]
			puissance=int(datas["tabVoiture"][idVoit]["puissance"])
			prix=int(datas["tabVoiture"][idVoit]["prix"])
			vitesseMax=int(datas["tabVoiture"][idVoit]["vitMax"])
			voiture=Voiture(idVoiture,modele,puissance,prix,vitesseMax)
		return voiture
	def searchSponsor(self,idSpons):
		with open('listeVoiture.json', 'r') as f:
			datas = json.load(f)
			idSponsor=int(datas["tabSponsor"][idSpons]["idSponsor"])
			nom=datas["tabSponsor"][idSpons]["nom"]
			idAdresse=int(datas["tabSponsor"][idSpons]["idAdresse"])
			adresse=self.searchAdresse(idAdresse)
			budget=int(datas["tabSponsor"][idSpons]["budget"])
			sponsor=Sponsor(idSponsor,nom,adresse,budget)
		return sponsor
	def searchEcurie(self,idEcurie):
		with open('listeVoiture.json', 'r') as f:
			datas = json.load(f)
			idEcurie=int(datas["tabEcurie"][idEcurie]["idEcurie"])
			nom=datas["tabEcurie"][idEcurie]["nom"]
			idAdresse=int(datas["tabEcurie"][idEcurie]["idAdresse"])
			adresse=self.searchAdresse(idAdresse)
			budget=int(datas["tabEcurie"][idEcurie]["budget"])
			ecurie=Ecurie(idEcurie,nom,adresse,budget)
		return ecurie
	def searchPilote(self,idPil):
		with open('listeVoiture.json', 'r') as f:
			datas = json.load(f)
			idPilote=int(datas["tabPilote"][idPil]["idPilote"])
			nom=datas["tabPilote"][idPil]["nom"]
			prenom=datas["tabPilote"][idPil]["prenom"]
			age=datas["tabPilote"][idPil]["age"]
			statut=datas["tabPilote"][idPil]["statut"]
			idVoiture=int(datas["tabPilote"][idPil]["idVoiture"])
			voiture=self.searchVoiture(idVoiture)
			pilote=Pilote(idPilote,nom,prenom,age,statut,voiture)
		return pilote
	def searchContrat(self,idContr):
		with open('listeVoiture.json', 'r') as f:
			datas = json.load(f)
			idContrat=int(datas["tabContrat"][idContr]["idContrat"])
			saison=datas["tabContrat"][idContr]["Saison"]
			idEcurie=int(datas["tabContrat"][idContr]["idEcurie"])
			ecurie=self.searchEcurie(idEcurie)
			idPilote=int(datas["tabContrat"][idContr]["idPilote"])
			pilote=self.searchPilote(idPilote)
			idCoPilote=int(datas["tabContrat"][idContr]["idCoPilote"])
			copilote=self.searchPilote(idCoPilote)
			idSponsor=int(datas["tabContrat"][idContr]["idSponsor"])
			sponsor=self.searchSponsor(idSponsor)
			idVoiture=int(datas["tabContrat"][idContr]["idVoiture"])
			voiture=self.searchVoiture(idVoiture)
			contrat=Contrat(idContrat,saison,ecurie,pilote,copilote,sponsor,voiture)
		return contrat

