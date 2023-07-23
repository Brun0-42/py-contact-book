# coding: utf-8

import logging

#---------------------------------------------------------------------------# 
class ContactName:
	def __init__(self, given_name, family_name):	
		self._given_name = given_name
		self._family_name = family_name
		self._additional = None
		self._prefix = None
		self._suffix = None

	def __str__(self):
		return str(self._given_name) + ' ' + str(self._family_name)

#---------------------------------------------------------------------------# 
class ContactAddress:
	def __init__(self):	
		self._street = None
		self._city = None
		self._zip_code = None
		self._country = None

	def __str__(self):
		return str(self._street) + ', ' + str(self._zip_code) + ', ' + str(self._city) + ', ' + str(self._country)

#---------------------------------------------------------------------------# 
class Contact:
	def __init__(self, given_name, family_name):
		self._log = logging.getLogger("contact")
		self._name = ContactName(given_name, family_name)
		self._address = ContactAddress()
		self._phone = None
		self._email = None

	def __str__(self):
		return str(self._name) + ' (address:' + str(self._address) + ', phone: ' + self._phone + ', email' + self._email + ')'


