# coding: utf-8

import logging
import optparse
import os

#---------------------------------------------------------------------------# 
class Config:
	def __init__(self):

		self._parser = optparse.OptionParser()
		self._parser.add_option("-v", "--verbosity", action="count", default=0,
			help='increase output verbosity')
		self._parser.add_option("-d", "--database", type=str, default="./db/contacts.db",
			help='contacts database file')
		self._parser.add_option("-k", "--encrypted-key", type=str,
			default="",
			help='encrypted key for contacts database file')
		self._log = logging.getLogger("config")

	def parse(self):
		(options, args) = self._parser.parse_args()

		self._database = options.database
		self._encrypted_key = options.encrypted_key

		self.verbosity = options.verbosity

	def check(self) -> bool:
		result = True

		if self._database == "":
			self._log.error("contacts database file is invalid")
			result = False
		else:
			if not os.path.exists(self._database):
				self._log.error("contacts database file not found")
				result = False

		return result

	def log(self, level = logging.INFO) -> None:
		self._log.log(level, "database file: {}".format(self._database))
		self._log.log(level, "encrypted_key: {}".format(self._encrypted_key))
		self._log.log(level, "verbosity    : {}".format(self.verbosity))
