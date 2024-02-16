
# from dbConnection import *
from flask import Flask
import json
import mysql.connector


cnx = mysql.connector.connect(user='root', password='',
                                host='127.0.0.1',
                                database='flask_studies',
                                use_pure=False)
cursor = cnx.cursor()

query = ("SELECT * FROM users")

    
cursor.execute(query)
rows = cursor.fetchall() 
json_output = json.dumps(rows)  
json_output2 = json.dumps(json_output)
print(rows)