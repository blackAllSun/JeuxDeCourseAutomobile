# coding=UTF-8
from Statut import *
from Voiture import *

class Pilote(object):
	"""
		:version:1.0
		:author:BlackAllSun
	"""
	""" ATTRIBUTES
		idPilote  (private)
		nom  (private)
		prenom  (private)
		age  (private)
		statut  (private)
		voiture  (private)
	"""
	def __init__(self,idPilote,nom,prenom,age,statut,voiture):
		self.idPilote=idPilote
		self.nom=nom
		self.prenom=prenom
		self.age=age
		self.statut=statut
		self.voiture=voiture
	def __getattr__(self,idPilote):
		getattr(self.strategy, idPilote)
	def __setattr__(self,idPilote,valueIDPilote):
		super(Pilote, self).__setattr__(idPilote,valueIDPilote)
	def __getattr__(self,nom):
		getattr(self.strategy, nom)
	def __setattr__(self,idNom,valueNom):
		super(Pilote, self).__setattr__(nom,valueNom)
	def __getattr__(self,prenom):
		getattr(self.strategy, prenom)
	def __setattr__(self,idPrenom,valuePrenom):
		super(Pilote, self).__setattr__(prenom,valuePrenom)
	def __getattr__(self,age):
		getattr(self.strategy, age)
	def __setattr__(self,age,valueAge):
		super(Pilote, self).__setattr__(age,valueAge)
	def __getattr__(self,statut):
		getattr(self.strategy, statut)
	def __setattr__(self,statut,valueStatut):
		super(Pilote, self).__setattr__(statut,valueStatut)
	def __getattr__(self,voiture):
		getattr(self.strategy, voiture)
	def __setattr__(self,voiture,valueVoiture):
		super(Pilote, self).__setattr__(voiture,valueVoiture)
	def __repr__(self):
		return "Pilote({}, {}, {}, {}, {})".format(repr(self.nom), repr(self.prenom), repr(str(self.age)), repr(str(self.statut)), repr(self.voiture))
	def __str__(self):
		return "{}, {},agé de {}, statut {}, conduisant {}".format(self.nom,self.prenom,elf.age,self.statut,self.voiture)

