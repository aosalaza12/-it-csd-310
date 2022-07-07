"""
Specification:
1.  Insert three new student documents. Make sure the documents match the fields I identified in the modeling assignment. 
    For the student_id’s use 1007, 1008, and 1009.
    To insert new documents you will need to use the insert_one() method.
    Note: refer to the MongoDB: insert_one() Example.
2.  Display the returned student_ids from the insert method calls.
    new_student_Id = students.insert_one(new_student_object).inserted_id. 
"""

import pymongo
from pymongo import MongoClient

myclient = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.cptgd.mongodb.net/")
mydb = myclient["pytech"]
mycol = mydb["students"]

print("-- INSERT STATEMENTS --")

# Insert Student 1
mydict = { "student_id": 1007, "first_name": "Alvaro", "last_name": "Salazar" }
mycol.insert_one(mydict)
print("Inserted student record", " ", mydict["first_name"], mydict["last_name"], " into the students collection with student_id ", mydict["student_id"])

#Insert Student 2
mydict = { "student_id": 1008, "first_name": "Frederic", "last_name": "Chopin"}
mycol.insert_one(mydict)
print("Inserted student record", " ", mydict["first_name"], mydict["last_name"], " into the students collection with student_id ", mydict["student_id"])

#Insert Student 3
mydict = { "student_id": 1009, "first_name": "Carl", "last_name":"Pascal"}
mycol.insert_one(mydict)
print("Inserted student record", " ", mydict["first_name"], mydict["last_name"], " into the students collection with student_id ", mydict["student_id"])

print()
print("End of program, press any key to exit...")
my_string = input()
print(my_string)

# Print Students documents
#
#docs = mycol.find({})
#for doc in docs:
#    print(doc)
