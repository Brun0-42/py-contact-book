# py-contact-book

An Contact Book Gui in python.

Example of execution:
``` 
python3 py-contact-book.py --database ./db/encrypted.db --encrypted-key 123456
```
## Requirements

Install this:
* Python_: <=3.10 (pip3 install -r requirements.txt)
* Sqlcipher (sudo apt install sqlcipher)

## For developers

### Create default database 

For create default database, use script "./db/create_default_db" or execute this procedure:

$ sqlcipher

sqlite> .open ./db/encrypted.db  
sqlite> PRAGMA key='123456';  
sqlite> CREATE TABLE IF NOT EXISTS tbl_contactlist (ID INTEGER PRIMARY KEY AUTOINCREMENT, col_family_name TEXT, col_given_name TEXT, col_additional_name TEXT, col_organisation TEXT, col_adress_street TEXT, col_adress_city TEXT, col_adress_zip_code TEXT, col_adress_country TEXT, col_phone TEXT, col_email TEX );  
sqlite> INSERT INTO tbl_contactlist (col_family_name, col_given_name, col_email, col_phone) VALUES ('John', 'Doe', 'tom@gmail.com', '123-456-7890');  
sqlite> .quit  
