"""
Author: Alvaro Salazar
Date: July 31, 2022. 

Specification:
    Using the example code I provided, connect to the pysports database.
    Using the example code I have provided, insert a new record into the player table for Team Gandalf.
        team_id = 1
    Using the example code I provided, execute a select query to display the player records (I want to verify the record was inserted successfully).
        This query should include the INNER JOIN; I want to see the team_name field and not the team_id in the output window.
    Using the example code I provided, update the newly inserted record by changing the player's team to Team Sauron.
        team_id = 2
    Using the example code I provided, execute a select query to display the updated record.
        This query should include the INNER JOIN; I want to see the team_name field and not the team_id in the output window.
    Using the example code I provided, execute a delete query to remove the updated record.
    Using the example code I provided, execute a select query to display all the records in the player table.
        This query should include the INNER JOIN; I want to see the team_name field and not the team_id in the output window.
"""

# from optparse import Values
import mysql.connector 
from mysql.connector import errorcode

## 2. Connect to the pysports DataBase

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
# End Connect         

# Cursor
cursor = db.cursor()

## 3. Insert a new record into the player table for Team Gandalf.

player_insert = "INSERT INTO player(first_name, last_name, team_id) VALUES('Smeagol', 'Shire Folk', 1)"
cursor.execute(player_insert)

## 4. Using a for loop, iterate over the cursor and display the results, to verify the record was inserted successfully.
 
player_select = "SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id ORDER BY player_id"

cursor.execute(player_select)

players_ij = cursor.fetchall()

# itera over cursor and display Player and team Table 

print()
print()
print("-- DISPLAYING PLAYERS AFTER INSERT --")
for playerij in players_ij:
    print("Player ID : {}".format(playerij[0]))
    print("First Name : {}".format(playerij[1]))
    print("Last Name : {}".format(playerij[2]))
    print("Team Name : {}".format(playerij[3]))
    print()


## 5. Update the newly inserted record by changing the player's team to Team Sauron - team_id = 2.


player_update = "UPDATE player SET team_id = 2 WHERE first_name = 'Smeagol'"
cursor.execute(player_update)

## 6. Using a for loop, iterate over the cursor and display the results, to verify the record was updated successfully.
 
player_select = "SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id"

cursor.execute(player_select)

players_ij = cursor.fetchall()

# itera over cursor and display Player and team Table 

print()
print()
print("-- DISPLAYING PLAYERS AFTER UPDATE --")
for playerij in players_ij:
    print("Player ID : {}".format(playerij[0]))
    print("First Name : {}".format(playerij[1]))
    print("Last Name : {}".format(playerij[2]))
    print("Team Name : {}".format(playerij[3]))
    print()


## 7. Execute a delete query to remove the updated record.

player_delete = "DELETE FROM player WHERE first_name = 'Smeagol'"
cursor.execute(player_delete)

## 8. Using a for loop, iterate over the cursor and display the results, to verify the record was updated successfully.
 
player_select = "SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id"

cursor.execute(player_select)

players_ij = cursor.fetchall()

# itera over cursor and display Player and team Table 

print()
print()
print("-- DISPLAYING PLAYERS AFTER DELETE --")
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
