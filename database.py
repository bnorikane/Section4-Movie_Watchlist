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
    release_timestamp REAL
);"""

CREATE_WATCHED_TABLE = """CREATE TABLE IF NOT EXISTS watched (
    watcher_name TEXT,
    title TEXT
);"""

INSERT_MOVIE = "INSERT INTO movies (title, release_timestamp) VALUES (?, ?);"
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > ?;"
SELECT_WATCHED_MOVIES = "SELECT * FROM watched;"
SET_MOVIE_WATCHED = "INSERT INTO watched (watcher_name, title) VALUES (?, ?);"

# Create database connection

connection = sqlite3.connect("data.db")

# Create tables in db
def create_tables():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)
        connection.execute(CREATE_WATCHED_TABLE)

########  PERFORM DATABASE ACTIONS IN RESPONSE TO USER MENU SELECTIONS

def add_movie(title, release_timestamp):
    with connection:
        connection.execute(INSERT_MOVIE, (title, release_timestamp))

# get all or upcoming movies
def get_movies(upcoming=False):
    with connection:
        cursor = connection.cursor()
        if upcoming:
            today_timestamp = datetime.datetime.today().timestamp()
            cursor.execute(SELECT_UPCOMING_MOVIES, (today_timestamp, ))
        else:
            cursor.execute(SELECT_ALL_MOVIES)
        return cursor.fetchall()

# add a new movie to the movies files
def watch_movie(watcher_name, movie_title):
    # print(movie_title, type(watcher_name, movie_title))
    with connection:
        connection.execute(SET_MOVIE_WATCHED, (watcher_name, movie_title ))

# get all watched movies by all watchers
def get_watched_movies():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_WATCHED_MOVIES)
        return cursor.fetchall()

