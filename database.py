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

import sqlite3

########  CREATE DATABASE AND TABLES 

def setup_movie_watch_db(dbname):
    # Create connection to movie_watch database
    conn = sqlite3.Connection(dbname)

    # Create movie table
    conn.execute( """CREATE TABLE IF NOT EXISTS movies 
                ( title TEXT, 
                release_date REAL,
                watched INTEGER);"""
                )
    return conn

########  PERFORM DATABASE ACTIONS IN RESPONSE TO USER MENU SELECTIONS

# 1) Add new movie




