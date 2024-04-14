def get_fav(title):
    c.execute("SELECT * FROM favorites WHERE title=?", (title,))
    return c.fetchall()

while True:
    response = input("v to visit, ls for list, add for new, rm to delete, q to quit: ")
    if response == "v":
        shortcut = input("What is the shortcut?: ")
        record = get_fav(shortcut)
        print(record)
        webbrowser.open(record[1])
    elif response == "ls":
        print("Listing")
    elif response == "add":
        print("adding")
    elif response == "rm":
        print("removing")
    elif response == "q":
        print("quitting")