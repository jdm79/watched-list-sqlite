import datetime
import database
#from database import add_movie, get_movies, watch_movie, get_watched_movies, create_tables

menu = """Please select one of the following options:
1) Add new movie
2) View upcoming movies
3) View all movies
4) Watch a movie
5) View watched movies
6) Exit

Your selection: """
welcome = "Welcome to the watchlist app!"


print(welcome)
database.create_tables()


def prompt_add_movie():
    title = input("Movie title: ")
    release_date = input("Release date (dd-mm-YYYY): ")
    # parse the string into a datetime object
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    timestamp = parsed_date.timestamp()

    database.add_movie(title, timestamp)


def print_movie_list(heading, movies):
    print("-- {heading} --")
    for movie in movies:
        movie_date = datetime.datetime.fromtimestamp(movie[1])
        human_date = movie_date.strftime("%b %d %Y")
        print(f"{movie[0]} (released on {human_date})")
    print("----- \n")

def print_watched_movie_list(username, movies):
    print("-- {username}'s watched movies --")
    for movie in movies:
        print(f"{movie[1]}")
    print("----- \n")


def prompt_watch_movie():
    username = input("Username: ")
    movie_title = input("Enter movie title you've watched: ")
    database.watch_movie(username, movie_title)


# using walrus operator below to refactor code 
while (user_input := input(menu)) != "6":
    if user_input == "1":
        prompt_add_movie()
        
    elif user_input == "2":
        movies = database.get_movies(True)
        print_movie_list("Upcoming", movies)

    elif user_input == "3":
        movies = database.get_movies()
        print_movie_list("All", movies)
    
    elif user_input == "4":
        prompt_watch_movie()
    
    elif user_input == "5":
        username = input("Username: ")
        movies = database.get_watched_movies(username)
        print_watched_movie_list(username, movies)
    
    else:
        print("Invalid option - please try again")
