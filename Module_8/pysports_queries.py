"""
Author: Alvaro Salazar
Date: July 29, 2022. 

Specification:
Write two select queries, one for the team table and one for the player table.
Example:
    SELECT team_id, team_name, mascot FROM team.
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
# 1. Team Table
 
cursor = db.cursor()

team_select = "SELECT team_id, team_name, mascot FROM team"

cursor.execute(team_select)

teams = cursor.fetchall()

# itera over cursor and display team table

print("-- DISPLAYING TEAM RECORDS --")
for team in teams:
    print("Team ID : {}".format(team[0]))
    print("Team Name : {}".format(team[1]))
    print("Mascot : {}".format(team[2]))
    print()


# 2. Player Table
 
player_select = "SELECT player_id, first_name, last_name, team_id FROM player"

cursor.execute(player_select)

players = cursor.fetchall()

# itera over cursor and display Player Table

print()
print()
print("-- DISPLAYING PLAYER RECORDS --")
for player in players:
    print("Player ID : {}".format(player[0]))
    print("First Name : {}".format(player[1]))
    print("Last Name : {}".format(player[2]))
    print("Team ID : {}".format(player[3]))
    print()
    
input("\n\n Press any key to continue...")

# Close Cursor and DB
cursor.close()
db.close()             

