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


# using walrus operator below to refactor code 
while (user_input := input(menu)) != "6":
    if user_input == "1":
        prompt_add_movie()
        
    elif user_input == "2":
        pass

    elif user_input == "3":
        pass
    
    elif user_input == "4":
        pass
    
    elif user_input == "5":
        pass
    
    else:
        print("Invalid option - please try again")
