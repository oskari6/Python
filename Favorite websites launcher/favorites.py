import sqlite3
import webbrowser

conn = sqlite3.connect(":memory:")
# conn = sqlite3.connect("fave.db")

c = conn.cursor()

# this is called seeding, hardcoding statements, testing
c.execute("CREATE TABLE IF NOT EXISTS favorites (title TEXT, url TEXT)")

def add_fav(title, url):
    c.execute("INSERT INTO favorites (title, url) VALUES (?, ?)", (title, url))
    conn.commit()

def remove_fav(title):
    c.execute("DELETE FROM favorites WHERE title=?", (title,))
    conn.commit()

def get_favs():
    c.execute("SELECT * FROM favorites")
    return c.fetchall()

def get_fav(title):
    c.execute("SELECT * FROM favorites WHERE title=?", (title,))
    return c.fetchall()

while True:
    response = input("v to visit, ls for list, add for new, rm to delete, q to quit: ")
    if response == "v":
        shortcut = input("What is the shortcut?: ")
        record = get_fav(shortcut)
        print(record)
        webbrowser.open(record[0][1])
    elif response == "ls":
        print(get_favs())
    elif response == "add":
        destination = input("Where do you want this shortcut to go?: ")
        shortcut = input("What is the shortcut?: ")
        add_fav(shortcut, destination)
    elif response == "rm":
        shortcut = input("What is the shortcut?: ")
        remove_fav(shortcut)
        print("removing")
    elif response == "q":
        print("quitting")
        exit()