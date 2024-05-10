""" Application and User Interface code for Movie Wathchlist
- S04 Movie Watchlist and Relational Data  

The project we'll be building in this section is a movie watchlist app. By the end of this section we'll have a project that allows users to:

- Keep track of movies they're interested in and their release dates.
- Store the movies a user has seen out of all movies in the database.
- Add a new user to keep track of their watched movies.

STAGE 1 - STORE AND RETRIEVE WATCHED MOVIES
- Single user and single table
- movies table (title, released_date, watched)
"""

import sqlite3

from database import setup_movie_watch_db

#### CONTSTANTS

welcome_text = "\nWelcome to the Watchlist App!\n"

menu_text = """
Please select one of the following options:

1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Add watched movie
5) View watched movies.
6) Add user to the app.
7) Exit.

your selection: """

#### FUNCTIONS

# 1) Add new movie
def prompt_add_movie():
    # get new movie entry from user
    movie_name = input("\n\tEnter Movie name: ")
    release_date = input("\tEnter release date (dd-mm-YYYY): ")
    # add new movie to database
    print(f"\n\tMovie name: {movie_name} \nRelease date: {release_date}")
    
# 2) View upcoming movies
def view_upcoming_movies():
    # get upcoming movies from db
    pass
    # display upcoming movies
    print("\n\tdisplay upcoming movies")

# 3) View all movies
def view_all_movies():
    # get all movies from db
    pass
    # display all movies
    print("\n\tdisplay all movies")

# 4) Add watched movie
def prompt_watched_movie():
    # get watched movie from user
    movie_name = input("\nEnter Movie name: ")
    # update movie to watched status in db
    print(f"\n\tUpdate Movie name: {movie_name} to watched status")

# 5) View watched movies
def view_watched_movies():
    # get all movies from db
    pass
    # display all movies
    print("\n\tdisplay watched movies")

# 6) Add user to the app
def prompt_add_user():
    # get new user
    user_name = input("\nEnter user name: ")
    # add user to db
    print(f"\n\tadd new user name: {user_name} to database")

# 7) Exit
    # Exit handled by walrus clause in while loop


#### MAIN

# Setup movie_watch database and get connection
conn = setup_movie_watch_db('movie_watch.sqlite')

# Show menu and get user response
while (user_input := input(menu_text)) != '7':
    # handle user response

    if user_input == "1":       # Add new movie
        prompt_add_movie()
        
    elif user_input == "2":     # View upcoming movies
        view_upcoming_movies()

    elif user_input == "3":     # View all movies
        # display all movies
        view_all_movies()

    elif user_input == "4":     # Add watched movie
        prompt_watched_movie()

    elif user_input == "5":     # View watched movies
        view_watched_movies()

    elif user_input == "6":     # Add user to the app
        prompt_add_user()
    else:
        print('INVALID RESPONSE: Please enter a number between 1 and 7!')




