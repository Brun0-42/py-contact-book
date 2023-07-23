#!/usr/bin/env python3

import logging
import sys
import src.config
import src.db
import src.gui

# ---------------------------------------------------------------------------- #
if __name__ == "__main__":
	config = src.config.Config()
	config.parse()

	logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s', datefmt='%d-%m-%y %H:%M:%S')
	log = logging.getLogger()
	log.setLevel(logging.WARNING)

	if not config.check():
		sys.exit(1)

	# Configure logger
	if int(config.verbosity) > 0:
		if int(config.verbosity) > 1:
			log.setLevel(logging.DEBUG)
		else:
			log.setLevel(logging.INFO)

	config.log()

	contacts_list = []
	db = src.db.Database(config._database, config._encrypted_key)
	db.load_contacts(contacts_list)

	# for contact in contacts_list:
	# 	print("contact: {}".format(str(contact)))

	gui = src.gui.ContactGui(contacts_list)
	gui.run()

	logging.info('Done')
