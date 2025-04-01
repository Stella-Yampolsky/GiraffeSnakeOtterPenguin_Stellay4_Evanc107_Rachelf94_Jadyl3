# GiraffeSnakeOtterPenguin: Stella, Moyo, Evan, Jady
# SoftDev
# April 2024

import sqlite3

DB_FILE="databse.db"

def createTables():
    createUsers()

# USER DATABASE FUNCTIONS------------------------------------------------------------------------------------------------
# edit data
def createUsers():
    users = sqlite3.connect(DB_FILE)
    c = users.cursor()
    command = "CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT, score INTEGER)"
    c.execute(command)
    users.commit()
def addUser(username, password):
    users = sqlite3.connect(DB_FILE)
    goodcharas = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345678910._-")
    if set(username).difference(goodcharas) or set(password).difference(goodcharas):
        return "There are special characters in the username or password."
    c = users.cursor()
    if (c.execute("SELECT 1 FROM users WHERE username=?", (username,))).fetchone() == None:
        c.execute("INSERT INTO users (username, password, score) VALUES (?, ?, ?)", (username, password, 0))
        users.commit()
        return
    return "Username taken."

# access information
def checkPassword(username, password):
    users = sqlite3.connect(DB_FILE)
    c = users.cursor()
    c.execute("SELECT city FROM users WHERE username=?", (username,))
    if c.fetchone() == None:
        return False
    c.execute("SELECT password FROM users WHERE username=?", (username,))
    res = c.fetchone()
    if (password != res[0]):
        return "Invalid login; please try again."
    return True
def getUsernameFromID(uid):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT username FROM users WHERE user_id =?", (uid,))
    if c.fetchone() == None:
        return "No such user"
    else:
        return c.fetchone()[0]
def getScoreFromID(uid):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT score FROM users WHERE user_id =?", (uid,))
    if c.fetchone() == None:
        return "No such user"
    else:
        return c.fetchone()[0]
def getScoreFromUsername(username):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT score FROM users WHERE username =?", (username,))
    if c.fetchone() == None:
        return "No such user"
    else:
        return c.fetchone()[0]

# dev stuff
def returnEntireUsersTable():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT * FROM users")
    return c.fetchall()

def deleteUsers():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("DROP table users")
