<<<<<<< HEAD
"""
Author: Alvaro Salazar
Date: July 13, 2022. 

Specification:
1. Add the required Python code to connect to the students collection (refer to previous assignments for help)
2. Call the find() method and output the documents to the terminal window.
3. Call the update_one method by student_id 1007 and update the last name to something different than the originally saved name.
4. Call the find_one method by student_id 1007 and output the document to the terminal window.
5. Styling guidelines:
   The format must match mine (this is gradable).
   You may use the data I have provided or supply your own values.
   The only exception is you must use student_id: 1007, 1008, and 1009.
"""

import pymongo
from pymongo import MongoClient

myclient = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.cptgd.mongodb.net/")
mydb = myclient["pytech"]
mycol = mydb["students"]

# Print students documents from find() method
print("-- DISPLAYING STUDENTS DOCUMENTS FROM FIND() QUERY --")

docs = mycol.find({})
for doc in docs:
    print("Student ID: ", doc["student_id"])
    print("First Name: ", doc["first_name"])
    print("Last Name : ", doc["last_name"])
    print()

# Updating student document from update_one() method 
#
doc1 = mycol.update_one({"student_id": 1007}, {"$set":{"last_name": "Jobs"}})

# Print a single document by student_id = 1007 from find.one() method
#
print("-- DISPLAYING STUDENT DOCUMENT 1007 --")
doc1 = mycol.find_one({"student_id": 1007})
print("Student ID: ", doc1["student_id"])
print("First Name: ", doc1["first_name"])
print("Last Name : ", doc1["last_name"])
print()
print()

print("End of program, press any key to continue...")
my_string = input()
print(my_string)

=======
>>>>>>> c1aaa5ab40cb99d288ca971c550716b33454c654

