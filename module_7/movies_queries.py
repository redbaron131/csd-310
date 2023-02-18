'''
Andrew Danielson
18 Jan 23
CSD310 Module 7.2
'''

import mysql.connector
from mysql.connector import errorcode


# Connect to the database
db = mysql.connector.connect(
	user = "movies_user",
	password= "popcorn",
	host= "127.0.0.1",
	database= "movies"
	)
cursor = db.cursor()

# Query 1: Select all fields for the studio table
query1 = 'SELECT * FROM studio;'
cursor.execute(query1)
studio_data = cursor.fetchall()
print('-- DISPLAYING Studio Data RECORDS--')
for row in studio_data:
    print(f'Studio ID: {row[0]}')
    print(f'Name: {row[1]}')
    print()

# Query 2: Select all fields for the genre table
query2 = 'SELECT * FROM genre;'
cursor.execute(query2)
genre_data = cursor.fetchall()
print('-- DISPLAYING Genre Data RECORDS--')
for row in genre_data:
    print(f'Genre ID: {row[0]}')
    print(f'Name: {row[1]}')
    print()

# Query 3: Select movie names for movies with run time less than two hours
query3 = 'SELECT film_name, film_runtime FROM film WHERE film_runtime < 120;'
cursor.execute(query3)
short_films = cursor.fetchall()
print('-- DISPLAYING Short Film RECORDS --')
for row in short_films:
    print(f'Film: {row[0]}')
    print(f'Runtime: {row[1]}')
    print()

# Query 4: Get a list of film names and directors ordered by director
query4 = 'SELECT film_name, film_director FROM film ORDER BY film_director;'
cursor.execute(query4)
films_by_director = cursor.fetchall()
print('-- DISPLAYING Films by Director in Order --')
for row in films_by_director:
    print(f'Film: {row[0]}')
    print(f'Director: {row[1]}')
    print()
  
# Close the connection
db.close()

input("\n\n Press any key to continue....")