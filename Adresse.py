# coding=UTF-8

class Adresse(object):

	"""
		:version:1.0
		:author:BlackAllSun
	"""
	""" ATTRIBUTES
		idAdresse  (private)
		ville  (private)
		pays  (private)

	"""
	def __init__(self,idAdresse,ville,pays): 
		self.idAdresse=idAdresse
		self.ville=ville
		self.pays=pays
	def __getattr__(self,idAdresse):
		getattr(self.strategy, idAdresse)
	def __setattr__(self,idAdresse,valueIDAdresse):
		super(Adresse, self).__setattr__(idAdresse,valueIDAdresse)
	def __getattr__(self,ville):
		getattr(self.strategy, ville)
	def __setattr__(self,ville,valueVille):
		super(Adresse, self).__setattr__(ville,valueVille)
	def __getattr__(self,pays):
		getattr(self.strategy, pays)
	def __setattr__(self,pays):
		super(Adresse, self).__setattr__(ville,valuePays)
	def __str__(self):
		return "id {}, ville {}, pays {}".format(repr(self.ville), repr(self.pays))
	def __repr__(self):
		return "Adresse({}, {})".format(repr(self.idAdresse), repr(self.ville), repr(self.pays))
