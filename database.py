""" 
Database access functions for Movie Watchlist app
- Keep track of movies they're interested in and their release dates.
- Store the movies a user has seen out of all movies in the database.
- Add a new user to keep track of their watched movies.


1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Add watched movie
5) View watched movies.
6) Add user to the app.
7) Exit.
"""

import sqlite3

# Create connection to movie_watch database
conn = sqlite3.Connection('movie_watch.sqlite')

# Create movie table
# create_movies_table_query = """
# CREATE TABLE IF NOT EXISTS movies (
#     name TEXT,
#     release_date TEXT
# );
# """

conn.execute("CREATE TABLE IF NOT EXISTS movies ( name TEXT, release_date TEXT );")

# Create user table

