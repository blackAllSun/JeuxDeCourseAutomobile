# coding=UTF-8

class Entreprise(object):
	"""
		:version:1.0
		:author:BlackAllSun
	"""
	""" ATTRIBUTES
		idEntreprise  (private)
		nom  (private)
		adresse  (private)
		budget  (private)
	"""
	def __init__(self,idEcurie,nom,adresse,budget):
		super().__init__(idEcurie,nom,adresse,budget)
		self.tabPilote=np.array([0,1])
	def __getattr__(self,idEntreprise):
		return self.idEntreprise
	def __setattr__(self,idEntreprise,valueIDEntreprise):
		super(Entreprise, self).__setattr__(idEntreprise,valueIDEntreprise)
	def __getattr__(self,nom):
		return self.nom
	def __setattr__(self,nom,valueNom):
		super(Entreprise, self).__setattr__(nom,valueNom)
	def __getattr__(self,adresse):
		return self.adresse
	def __setattr__(self,adresse,valueAdresse):
		super(Entreprise, self).__setattr__(adresse,valueAdresse)
	def __repr__(self):
		return "Entreprise({}, {})".format(repr(self.nom), repr(self.adresse), repr(str(self.budget)))
	def __str__(self):
		return "{} logé à {}, avec un budget de {} €".format(self.nom,self.adresse,str(self.budget))

