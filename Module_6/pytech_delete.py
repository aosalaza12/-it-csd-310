"""
Author: Alvaro Salazar
Date: July 14, 2022. 

Specification:
1. Add the required Python code to connect to the students collection (refer to previous assignments for help)
2. Call the find() method and output the documents to the terminal window.
3. Call the insert_one() method and Insert a new document into the pytech collection with student_id 1010.
4. Call the find_one method and output the document to the terminal window.
5. Call the delete_one() method by student_id 1008 
6. Call the find() method and output the documents to the terminal window.
7. Styling guidelines:
   The format must match mine (this is gradable).
   You may use the data I have provided or supply your own values.
   The only exception is you must use student_id: 1007, 1008, 1009, and 1010.
"""

import pymongo
from pymongo import MongoClient

myclient = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.cptgd.mongodb.net/")
mydb = myclient["pytech"]
mycol = mydb["students"]

# Print students documents from find() method, before insert and delete 
print("-- DISPLAYING STUDENTS DOCUMENTS FROM FIND() QUERY --")

docs = mycol.find({})
for doc in docs:
    print("Student ID: ", doc["student_id"])
    print("First Name: ", doc["first_name"])
    print("Last Name : ", doc["last_name"])
    print()

# Inserting student document 1010 from insert_one() method 
#
print("-- INSERT STATEMENTS --")
mydict = { "student_id": 1010, "first_name": "Steve", "last_name": "Salazar" }
mycol.insert_one(mydict)
doc1 = mycol.find_one({"student_id": 1010})

print("Inserted student record into the students collection with document_id ",doc1["_id"])
print()

print("-- DISPLAYING STUDENT TEST DOC --")
print("Student id : ", doc1["student_id"])
print("First Name : ", doc1["first_name"])
print("Last Name  : ", doc1["last_name"])
print()

# Deleting student_id 1008 from delete_one method
#
mycol.delete_one({"student_id": 1008})

# Print Students Documents from find() method, after insert student id 1010, and delete student id 1008
#
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

docs = mycol.find({})
for doc in docs:
    print("Student ID: ", doc["student_id"])
    print("First Name: ", doc["first_name"])
    print("Last Name : ", doc["last_name"])
    print()
    print()


print("End of program, press any key to continue...")
my_string = input()
print(my_string)
