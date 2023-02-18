"""
Andrew Danielson
18 Jan 23
CSD310 Module 8.2
"""

import mysql.connector
from mysql.connector import errorcode


# Connect to the database
db = mysql.connector.connect(
    user="movies_user", password="popcorn", host="127.0.0.1", database="movies"
)
cursor = db.cursor()

# function to show films
def show_films():
    cursor.execute("SELECT film.film_name, film.film_director, genre.genre_name, studio.studio_name FROM film JOIN studio ON film.studio_id = studio.studio_id JOIN genre ON film.genre_id = genre.genre_id")
    print('-- DISPLAYING FILMS--')
    for row in cursor.fetchall():
        print("Film Name: ", row[0])
        print("Director: ", row[1])
        print("Genre Name: ", row[2])
        print("Studio Name: ", row[3])
        print()

show_films()

def show_films1():
    cursor.execute("SELECT film.film_name, film.film_director, genre.genre_name, studio.studio_name FROM film JOIN studio ON film.studio_id = studio.studio_id JOIN genre ON film.genre_id = genre.genre_id")
    print('-- DISPLAYING FILMS AFTER INSERT--')
    for row in cursor.fetchall():
        print("Film Name: ", row[0])
        print("Director: ", row[1])
        print("Genre Name: ", row[2])
        print("Studio Name: ", row[3])
        print()

# insert statement to add a new studio
cursor.execute(
    "INSERT INTO studio (studio_id, studio_name) VALUES (4, 'Walt Disney Studios'), (5, 'Pixar Animation Studios')"
)
# insert statement to add a new genre
cursor.execute("INSERT INTO genre (genre_id, genre_name) VALUES (4, 'Adventure')")
# insert statement to add a new film into the film table
cursor.execute(
    "INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) VALUES ('Jurassic Park', '1993', '127', 'Steven Spielberg', 3, 2), ('The Lion King', '1994', '88', 'Roger Allers', 4, 3), ('Up', '2009', '96', 'Pete Docter', 5, 4)"
)

show_films1()

def show_films2():
    cursor.execute("SELECT film.film_name, film.film_director, genre.genre_name, studio.studio_name FROM film JOIN studio ON film.studio_id = studio.studio_id JOIN genre ON film.genre_id = genre.genre_id")
    print('-- DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror --')
    for row in cursor.fetchall():
        print("Film Name: ", row[0])
        print("Director: ", row[1])
        print("Genre Name: ", row[2])
        print("Studio Name: ", row[3])
        print()

# update statement to change film genre 
cursor.execute("UPDATE film SET genre_id = 1 WHERE film_name = 'Alien'")

show_films2()

def show_films3():
    cursor.execute("SELECT film.film_name, film.film_director, genre.genre_name, studio.studio_name FROM film JOIN studio ON film.studio_id = studio.studio_id JOIN genre ON film.genre_id = genre.genre_id")
    print('-- DISPLAYING FILMS AFTER DELETE--')
    for row in cursor.fetchall():
        print("Film Name: ", row[0])
        print("Director: ", row[1])
        print("Genre Name: ", row[2])
        print("Studio Name: ", row[3])
        print()

# delete statement to delete a film  
cursor.execute("DELETE FROM film WHERE film_name = 'Gladiator'")

show_films3()


#show_films()


# Close the cursor and connection
cursor.close()
db.close()

input("\n\n Press any key to continue....")
