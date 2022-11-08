from pymongo import MongoClient
import os

#username and pw are passed via the .env file for extra sec B)
username = os.environ.get('USER') 
password = os.environ.get('PASSWORD')

#connect to our client
client = MongoClient("mongodb+srv://" + username + ":" + password + "@anuradb.rrmor6f.mongodb.net/?retryWrites=true&w=majority")

#selecting the DataBase 
db = client.test

#selecting the Connection
coll = db.dummyData

#just some random dummy data
dummyData = [
	{"name": "Halley's Comet", "officialName": "1P/Halley", "orbitalPeriod": 75, "radius": 3.4175, "mass": 2.2e14},
	{"name": "Wild2", "officialName": "81P/Wild", "orbitalPeriod": 6.41, "radius": 1.5534, "mass": 2.3e13},
	{"name": "Comet Hyakutake", "officialName": "C/1996 B2", "orbitalPeriod": 17000, "radius": 0.77671, "mass": 8.8e12},
]

#inserting the data into the collection 
result = coll.insert_many(dummyData)

#printing the ids of the inserted objects
print(result.inserted_ids)

#close connection, cause we care 
client.close()
