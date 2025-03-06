from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')

db = client.Andulasia_Health

doctors = db.doctors
