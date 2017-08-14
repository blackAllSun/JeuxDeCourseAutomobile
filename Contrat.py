# coding=UTF-8
from Saison import *
from Ecurie import *
from Pilote import *
from Sponsor import *
from Voiture import *

class Contrat(object):

	"""
		:version:1.0
		:author:BlackAllSun
	"""
	""" ATTRIBUTES
		idContrat  (private)
		saison  (private)
		ecurie  (private)
		pilote  (private)
		copilote  (private)
		sponsor  (private)
		voiture  (private)
	"""
	def __init__(self,idContrat,saison,ecurie,pilote,copilote,sponsor,voiture):
		self.idContrat=idContrat
		self.saison=saison
		self.ecurie=ecurie
		self.pilote=pilote
		self.copilote=copilote
		self.sponsor=sponsor
		self.voiture=voiture
	def __getattr__(self,idContrat):
		getattr(self.strategy, idContrat)
	def __setattr__(self,idContrat,valueIDContrat):
		super(Contrat, self).__setattr__(idContrat,valueIDContrat)
	def __getattr__(self):
		getattr(self.strategy, saison)
	def __setattr__(self,saison,valueSaison):
		super(Contrat, self).__setattr__(saison,valueSaison)
	def __getattr__(self,ecurie):
		getattr(self.strategy, ecurie)
	def __setattr__(self,ecurie,valueEcurie):
		super(Contrat, self).__setattr__(ecurie,valueEcurie)
	def __getattr__(self,pilote):
		getattr(self.strategy, pilote)
	def __setattr__(self,pilote,valuePilote):
		super(Contrat, self).__setattr__(pilote,valuePilote)
	def __getattr__(self,copilote):
		getattr(self.strategy, copilote)
	def __setattr__(self,copilote,valueCoPilote):
		super(Contrat, self).__setattr__(copilote,valueCoPilote)
	def __repr__(self):
		return "Contrat({}, {})".format(repr(self.saison), repr(self.ecurie), repr(self.pilote), repr(self.copilote))
	def __str__(self):
		return "saison {}, ecurie {}, pilote {}, copilote {}".format(self.saison,self.ecurie,self.pilote,self.copilote)

