__author__ = 'piotrk'

import pymongo

uri = 'mongodb://127.0.0.1:27017'
client = pymongo.MongoClient(uri)
database = client['fullstack']
collection = database['students']

students = [student['name'] for student in collection.find({}) if student['name'] == 'Jose']
print(students)