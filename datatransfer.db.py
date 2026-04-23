#DATABASE STATUS: Established
#Table Name: data
#Storage: emailphishingdatastorage.db

#NOTE: The 'data' table and its schema (including 'domain' and 'score' columns) 
#have been manually established via SQLite3 CLI. This script focuses 
#strictly on data connection and transfer.

import sqlite3

connection = sqlite3.connect(r"C:\Users\eshab\emailphishingdatastorage.db")
cursor = connection.cursor()
# cursor.execute("ALTER TABLE data ADD COLUMN domain TEXT")
# cursor.execute("ALTER TABLE data ADD COLUMN score INTEGER")
connection.commit()
connection.close()
