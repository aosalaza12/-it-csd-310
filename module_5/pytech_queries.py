"""
Specification:
1.  Use the find() method to display all documents in the collection.
    -   students.find({})
    -   Note: refer to the find() Example.
2.  Use the findOne() method to display a single document by student_id.
    -   students.find_one({“student_id”: “1007”})
    -   Note: refer to the find_one() Example.
"""

import pymongo
from pymongo import MongoClient

myclient = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.cptgd.mongodb.net/")
mydb = myclient["pytech"]
mycol = mydb["students"]


# Print all documents in Students collection
#
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

docs = mycol.find({})
for doc in docs:
    print("Student ID: ", doc["student_id"])
    print("First Name: ", doc["first_name"])
    print("Last Name : ", doc["last_name"])
    print()

# Print a single document by student_id
#
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find_one() QUERY --")
doc1 = mycol.find_one({"student_id": 1008})

print("Student ID: ", doc1["student_id"])
print("First Name: ", doc1["first_name"])
print("Last Name : ", doc1["last_name"])
print()
print()

print("End of program, press any key to exit...")
my_string = input()
print(my_string)

#for doc in docs:
#    print(doc)
