# coding: utf-8

import logging
import sqlite3

import src.contact

#---------------------------------------------------------------------------# 
class Database:
	def __init__(self, file, key):
		self._log = logging.getLogger("db")
		self._log.debug("open database (file: {} / key: {})".format(file, key))
		self._conn = sqlite3.connect(file)
		self._cursor = self._conn.cursor()
		self._cursor.execute( "PRAGMA key = '" + key + "';" )

	def __del__(self):
		self._log.debug("close database")
		self._conn.close()

	def load_contacts(self, contacts_list):
		sql_query = "SELECT * FROM tbl_contactlist ORDER BY LOWER(col_family_name) ASC"
		self._cursor.execute(sql_query)
		rows = self._cursor.fetchall()

		for row in rows:
			contact = src.contact.Contact(row[1], row[2])
			contact._name._additional = row[3]
			contact._name._suffix = row[4]
			contact._address._street = row[5]
			contact._address._city = row[6]
			contact._address._zip_code = row[7]
			contact._address._country = row[8]
			contact._phone = row[9]
			contact._email = row[10]
			contacts_list.append(contact)
