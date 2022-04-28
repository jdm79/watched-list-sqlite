import database

# this variable will be passed to the user function
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

# using walrus operator below to refactor code 
while (user_input := input(menu)) != "6":
    if user_input == "1":
        prompt_new_entry()
        
    elif user_input == "2":
        view_entries(get_entries())

    elif user_input == "3":
        pass
    
    elif user_input == "4":
        pass
    
    elif user_input == "5":
        pass
    
    else:
        print("Invalid option - please try again")

# def prompt_new_entry():
#     entry_content = input("What have you learned today? ")
#     entry_date = input("Enter the date: ")

#     add_entry(entry_content, entry_date)

# def view_entries(entries):
#     for entry in entries:
#         print(f"\n{entry['date']}\n{entry['content']}\n")




