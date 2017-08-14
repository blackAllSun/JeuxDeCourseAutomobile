# coding=UTF-8
from Entreprise import *

class Sponsor (Entreprise):
	"""
		:version:1.0
		:author:BlackAllSun
	"""
	def __init__(self,idSponsor,nom,adresse,budget):
		super().__init__(idSponsor,nom,adresse,budget)

