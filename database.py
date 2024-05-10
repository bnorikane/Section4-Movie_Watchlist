""" 
Database access functions for Movie Watchlist app
- Keep track of movies they're interested in and their release dates.
- Store the movies a user has seen out of all movies in the database.
- Add a new user to keep track of their watched movies.

Database functions

One time actions:
    create db
        movie_watch
    create tables
        movies

User menu actions
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Add watched movie
5) View watched movies.
6) Add user to the app.
7) Exit.
"""

import datetime
import sqlite3

########  CREATE DATABASE AND TABLES 

# Define query strings
CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies (
    title TEXT, 
    release_timestamp REAL,
    watched INTEGER
);"""

INSERT_MOVIE = "INSERT INTO movies (title, release_timestamp, watched) VALUES (?, ?, 0);"
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > ?;"
SELECT_WATCHED_MOVIES = "SELECT * FROM movies WHERE watched = 1;"

# Create database connection

connection = sqlite3.connect("data.db")

# Create tables in db
def create_tables():
    pass

########  PERFORM DATABASE ACTIONS IN RESPONSE TO USER MENU SELECTIONS

def add_movie(title, release_timestamp):
    pass

def get_movies(upcoming=False):
    pass

def watch_movie(movie_title):
    pass

def get_watched_movies():
    pass

