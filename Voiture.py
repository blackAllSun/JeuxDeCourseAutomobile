# coding=UTF-8

class Voiture(object):
	"""
		:version:1.0
		:author:BlackAllSun
	"""
	""" ATTRIBUTES
		idVoit  (private)
		modele  (private)
		puissance  (private)
		prix  (private)
		vitMax  (private)
	"""
	def __init__(self,idVoit,modele,puissance,prix,vitMax):
		self.idVoit=int(idVoit)
		self.modele=modele
		self.puissance=puissance
		self.prix=prix
		self.vitMax=vitMax
	def __getattr__(self,idAdresse):
		getattr(self.strategy, idAdresse)
	def __setattr__(self,idAdresse,valueIDAdresse):
		super(Voiture, self).__setattr__(idAdresse,valueIDAdresse)
	def __getattr__(self,modele):
		getattr(self.strategy, modele)
	def __setattr__(self,modele,valueModele):
		super(Voiture, self).__setattr__(modele,valueModele)
	def __getattr__(self,puissance):
		getattr(self.strategy, puissance)
	def __setattr__(self,puissance,valuePuissance):
		super(Voiture, self).__setattr__(puissance,valuePuissance)
	def __getattr__(self,prix):
		getattr(self.strategy, prix)
	def __setattr__(self,prix,valuePrix):
		super(Voiture, self).__setattr__(prix,valuePrix)
	def __getattr__(self,vitMax):
		getattr(self.strategy, vitMax)
	def setVitMax(self,vitMax,valueVitMax):
		super(Voiture, self).__setattr__(prix,valueVitMax)
	def __repr__(self):
		return "Voiture({}, {})".format(repr(self.modele), repr(str(self.puissance)), repr(str(self.prix)), repr(str(self.vitMax)))
	def afficher(self):
		print(str(self.modele)," ",str(self.puissance)," ",str(self.prix)," ",str(self.vitMax))

