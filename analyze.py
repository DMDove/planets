import sqlite3
connection=sqlite3.connect("survey.db")
cursor=connection.cursor()
cursor.execute("Select Site.lat, Site.long from SITE;")
results = cursor.fetchall()
for r in results:
	print(r)
cursor.close()
connection.close()