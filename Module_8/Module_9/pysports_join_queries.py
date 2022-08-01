"""
Author: Alvaro Salazar
Date: July 30, 2022. 

Specification:
    create an INNER JOIN query to connect the player and team tables by team_id and display the results
"""

import mysql.connector 
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "Csx01da1$",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True,
#    "auth_plugin":"mysql_native_password"
}

try:
#    db = mysql.connector.connect(**config)
    db = mysql.connector.connect(user='pysports_user', password='Csx01da1$',
                              host='127.0.0.1', database='pysports',
                              auth_plugin='mysql_native_password')
    
    print("\n Database user {} connected to MySQL on host {} with database {} ".format(config["user"], config["host"], config["database"] ))
    
#    input("\n\n Press any key to continue...")
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")
        
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist ")
        
    else:
        print(err)
        

# Using a for loop, iterate over the cursor and display the results.
 
cursor = db.cursor()

# 2. Player Table
 
player_inner_join = "SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id"

cursor.execute(player_inner_join)

players_ij = cursor.fetchall()

# itera over cursor and display Player and team Table 

print()
print()
print("-- DISPLAYING PLAYER RECORDS --")
for playerij in players_ij:
    print("Player ID : {}".format(playerij[0]))
    print("First Name : {}".format(playerij[1]))
    print("Last Name : {}".format(playerij[2]))
    print("Team Name : {}".format(playerij[3]))
    print()
    
input("\n\n Press any key to continue...")

# Close Cursor and DB
cursor.close()
db.close()             
