# coding=UTF-8
from Entreprise import *
from Statut import *
from Voiture import *
from Saison import *

class Ecurie (Entreprise):

	"""
		:version:1.0
		:author:BlackAllSun
	"""

	def addPilote(self, idPilote, nom, prenom, age, statut, voiture, saison):
		"""
			@param int idPilote : 
			@param string nom : 
			@param string prenom : 
			@param int age : 
			@param Statut statut : 
			@param Voiture voiture : 
			@param Saison saison : 
			@return  : pilote
			@author : BlackAllSun
		"""
		if tabPilote[idPilote] in 0:
			pilote=Pilote(self,nom,prenom,age,Statut.PILOTE,voiture,saison)
			self.tabPilote.append(pilote)
			return pilote
		elif tabPilote[idPilote] in 1:
			pilote=Pilote(self,nom,prenom,age,Statut.CO_PILOTE,voiture,saison)
			self.tabPilote.append(pilote)
			return pilote
	def __init__(self,idEcurie,nom,adresse,budget):
		super().__init__(idEcurie,nom,adresse,budget)
		self.tabPilote=np.array([0,1])
	def __repr__(self):
		return "Ecurie({}, {}, {})".format(repr(self.nom),repr(self.adresse),repr(str(self.budget)))

		


