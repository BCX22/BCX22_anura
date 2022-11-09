from pymongo import MongoClient
import os
import csv

#username and pw are passed via the .env file for extra sec B)
username = os.environ.get('USER') 
password = os.environ.get('PASSWORD')

#connect to our client
client = MongoClient("mongodb+srv://" + username + ":" + password + "@anuradb.rrmor6f.mongodb.net/?retryWrites=true&w=majority")

#selecting the DataBase 
db = client.anuracsv

#selecting the Collection
coll = db.dummyData


dummyData = []

with open('vitaldata.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		coll.insert_one(row)


#close connection, cause we care 
client.close()
