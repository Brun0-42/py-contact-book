#!/usr/bin/env python3

import sqlite3

# ---------------------------------------------------------------------------- #
if __name__ == "__main__":
	conn = sqlite3.connect('./encrypted.db')
	cursor = conn.cursor()
	cursor.execute( "PRAGMA key = '123456';" )

	sql_query = "CREATE TABLE IF NOT EXISTS tbl_contactlist (ID INTEGER PRIMARY KEY AUTOINCREMENT, col_family_name TEXT, col_given_name TEXT, col_additional_name TEXT, col_organisation TEXT, col_adress_street TEXT, col_adress_city TEXT, col_adress_zip_code TEXT, col_adress_country TEXT, col_phone TEXT, col_email TEX );"
	cursor.execute(sql_query)

	sql_query = "INSERT INTO tbl_contactlist (col_family_name, col_given_name, col_email, col_phone) VALUES ('John', 'Doe', 'tom@gmail.com', '123-456-7890');"
	cursor.execute(sql_query)
	conn.commit()

	conn.close()

