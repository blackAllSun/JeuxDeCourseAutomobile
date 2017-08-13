#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pojo.py
#  
#  Copyright 2017 BlackAllSun <attilavlh10@gmail.com>
#  
#  
from pprint import pprint
import json
from pojo import *
from numpy import array
import numpy as np
from enum import Enum 
class Adresse(object):
	def __init__(self,ville,pays):
		self.ville=ville
		self.pays=pays
	def getVille(self):
		return self.ville
	def setVille(self,ville):
		self.ville=ville
	def getPays(self):
		return self.pays
	def setPays(self,pays):
		self.pays=pays
	def afficher(self):
		print("Adresse ville : ",self.ville," pays : ",self.pays) 
	def toString(self):
		return self.ville+" "+self.pays
class Entreprise(object):
	def __init__(self,nom,adresse,budget):
		self.nom=nom
		self.adresse=adresse
		self.budget=budget
	def getNom(self):
		return self.nom
	def setNom(self,nom):
		self.nom=nom
	def getAdresse(self):
		return self.adresse
	def setAdresse(self,adresse):
		self.adresse=adresse
	def getBudget(self):
		return self.budget
	def setBudget(self,budget):
		self.budget=budget
	def afficher(self):
		print("Entreprise nom : ",self.nom," adresse : ",self.adresse.toString()," budget : ",self.budget)
class Ecurie(Entreprise):

	def __init__(self,nom,adresse,budget):
		super().__init__(nom,adresse,budget)
		self.tabPilote=np.array([0,1])
		self.tabVoiture=np.array(range(0,11,1))
	def addPilote(self,idPilote,nom,prenom,age,voiture,saison):
		if tabPilote[idPilote] in 0:
			pilote=Pilote(self,nom,prenom,age,Statut.PILOTE,voiture,saison)
			return pilote
		elif tabPilote[idPilote] in 1:
			pilote=Pilote(self,nom,prenom,age,Statut.CO_PILOTE,voiture,saison)
			self.tabPilote.append(pilote)
			return pilote
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
			self.tabVoiture[idVoiture]=voiture
		return voiture
	def toString(self):
		return self.nom+" "+self.adresse.toString()+" "+str(self.budget)
	def afficher(self):
		return "Ecurie : ",self.nom," ",self.adresse.toString()," budget",str(self.budget)
class Voiture(object):
	def __init__(self,idVoit,modele,puissance,prix,vitMax):
		self.idVoit=int(idVoit)
		self.modele=modele
		self.puissance=puissance
		self.prix=prix
		self.vitMax=vitMax
	def getModele(self):
		return self.modele
	def setModele(self,modele):
		self.modele=modele
	def getPuissance(self):
		return self.puissance
	def setPuissance(self,puissance):
		self.puissance=puissance
	def getPrix(self):
		return self.prix
	def setPrix(self,prix):
		self.prix=prix
	def getVitMax(self):
		return self.vitMax
	def setVitMax(self,vitMax):
		self.vitMax=vitMax
	def toString(self):
		return str(self.modele)+" "+str(self.puissance)+" "+str(self.prix)+" "+str(self.vitMax)
	def afficher(self):
		print(str(self.modele)," ",str(self.puissance)," ",str(self.prix)," ",str(self.vitMax))
class Statut(Enum):
    PILOTE = 1
    CO_PILOTE = 2
class Saison(Enum):
	PRINTEMPS=1
	ETE=2
	AUTONOMNE=3
	HIVER=4
class Pilote(object):
	def __init__(self,nom,prenom,age,statut,voiture,saison):
		self.nom=nom
		self.prenom=prenom
		self.age=age
		self.statut=statut
		self.voiture=voiture
		self.saison=saison
	def toString(self):
		return self.nom+" "+self.prenom+" "+str(self.age)+" "+str(self.statut)+" "+self.voiture.toString()+" "+str(self.saison)
	def afficher(self):
		print("Pilote : ",self.nom," ",self.prenom," ",str(self.age)," ",str(self.statut)," ",self.voiture.toString()," ",str(self.saison))
class Contrat(object):
	def __init__(self,saison,ecurie,pilote,copilote):
		self.saison=saison
		self.ecurie=ecurie
		self.pilote=pilote
		self.copilote=copilote
	def getSaison(self):
		return self.saison
	def setSaison(self,saison):
		self.saison=saison
	def getEcurie(self):
		return self.ecurie
	def setEcurie(self):
		self.ecurie=ecurie
	def getPilote(self):
		return self.pilote
	def setPilote(self,pilote):
		self.pilote=pilote
	def getCoPilote(self):
		return self.copilote 
	def setCoPilote(self,copilote):
		self.copilote=copilote
	def toString(self):
		return self.saison+" "+self.ecurie.toString()+" "+self.pilote.toString()+" "+self.copilote.toString()
	def afficher(self):
		print("Contrat : ",self.saison," ",self.ecurie.toString()," ",self.pilote.toString()," ",self.copilote.toString())
