""" Application and User Interface code for Movie Wathchlist
- S04 Movie Watchlist and Relational Data  

The project we'll be building in this section is a movie watchlist app. By the end of this section we'll have a project that allows users to:

- Keep track of movies they're interested in and their release dates.
- Store the movies a user has seen out of all movies in the database.
- Add a new user to keep track of their watched movies.

STAGE 1 - STORE AND RETRIEVE WATCHED MOVIES
- Single user and single table
- movies table (title, released_date, watched)

STAGE 2 - ADD MULTIUSER WATCHLISTS
- Separate movies and watchlist tables - imperfect
- watched table (watcher_name TEXT, title TEXT)
- movies table (title TEXT, release_timestamp REAL)
"""

import sqlite3
import datetime

import database

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

print(welcome_text)
database.create_tables()

#### FUNCTIONS

# 1) Add new movie
def prompt_add_movie():
    # get new movie entry from user
    movie_title = input("\n\tEnter Movie title: ")
    release_date = input("\tEnter release date (dd-mm-YYYY): ")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y" )
    timestamp = parsed_date.timestamp()

    # add new movie to database
    database.add_movie(movie_title, timestamp)
    
# 2) View upcoming movies
def view_upcoming_movies():
    upcoming_movies = database.get_movies(upcoming=True)
    print_movie_list("Upcoming", upcoming_movies)

# 3) View all movies
def view_all_movies():
    # get all movies from db
    all_movies = database.get_movies()
    print_movie_list("All", all_movies)

# 4) Add watched movie
def prompt_watched_movie():
    # get watched movie from user
    watcher_name = input("\nEnter watcher's name: ")
    movie_title = input("\nEnter Movie title: ")
    # update movie to watched status in db
    database.watch_movie(watcher_name, movie_title)

# 5) View watched movies
def view_watched_movies():
    # get all movies from db
    watched_movies = database.get_watched_movies()
    print_watched_movies("Watched", watched_movies)

# 6) Add user to the app
def prompt_add_user():
    # get new user
    user_name = input("\nEnter user name: ")
    # add user to db
    print(f"\n\tadd new user name: {user_name} to database")

# 7) Exit
    # Exit handled by walrus clause in while loop

# print list of movies
def print_movie_list(heading, movies):
    print(f"-- {heading} Movies --")
    for movie in movies:
        movie_date = datetime.datetime.fromtimestamp(movie[1])
        human_date = movie_date.strftime("%d %b %Y")
        print(f'"{movie[0]}" released on {human_date}'
        )
    print("---- \n")

# print watched movies
def print_watched_movies(heading, watched_movies):
    print(f"---- {heading} Movies ----")
    for watched in watched_movies:
        # movie_date = datetime.datetime.fromtimestamp(movie[1])
        # human_date = movie_date.strftime("%d %b %Y")
        print(f'"{watched[1]}" watched by {watched[0]}'
        )
    print("---- \n")



#### MAIN

# Create database connection
connection = sqlite3.connect("data.db")
# Create tables in db
database.create_tables()

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




