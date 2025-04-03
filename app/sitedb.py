# GiraffeSnakeOtterPenguin: Stella, Moyo, Evan, Jady
# SoftDev
# April 2024

import sqlite3

DB_FILE="databse.db"

def createTables():
    createUsers()
    createPlays()

# USER DATABASE FUNCTIONS------------------------------------------------------------------------------------------------
# edit data
def createUsers():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT, score INTEGER, numPlays INTEGER)"
    c.execute(command)
    db.commit()
def addUser(username, password):
    db = sqlite3.connect(DB_FILE)
    goodcharas = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345678910._-")
    if set(username).difference(goodcharas) or set(password).difference(goodcharas):
        return "There are special characters in the username or password."
    c = db.cursor()
    if (c.execute("SELECT 1 FROM users WHERE username=?", (username,))).fetchone() == None:
        c.execute("INSERT INTO users (username, password, score, numPlays) VALUES (?, ?, ?, ?)", (username, password, 0, 0))
        db.commit()
        return
    return "Username taken."
def changeScore(username, score):
    db = sqlite3.connect(USER_FILE)
    c = db.cursor()
    if (c.execute("SELECT 1 FROM users WHERE username=?", (username,))).fetchone() == None:
        return
    c.execute("UPDATE users SET score=? WHERE username=?", (score, username))
    db.commit()
def incrementnumPlays(username):
    db = sqlite3.connect(USER_FILE)
    c = db.cursor()
    if (c.execute("SELECT 1 FROM users WHERE username=?", (username,))).fetchone() == None:
        return
    c.execute("UPDATE users SET numPlays=? WHERE username=?", (getnumPlaysFromUsername(username)+1, username))
    db.commit()
def changeScoreUID(uid, score):
    changeScore(getUsernameFromID(uid), score)
def incrementnumPlaysUID(uid):
    incrementnumPlays(getUsernameFromID(uid))

# access information
def checkPassword(username, password):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
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
def getIDFromUsername(username):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT user_id FROM users WHERE username =?", (username,))
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
def getnumPlaysFromUsername(username):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT numPlays FROM users WHERE username =?", (username,))
    if c.fetchone() == None:
        return "No such user"
    else:
        return c.fetchone()[0]
def getnumPlaysFromID(uid):
    return getnumPlaysFromUsername(getUsernameFromID(uid))

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

# PLAY TABL;E ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#create and change data
def createPlays():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = '''CREATE TABLE IF NOT EXISTS plays (user_id INTEGER, player_id INTEGER, name TEXT, age INTEGER, health INTEGER,
                mental_health INTEGER, address TEXT,
                alcoholism INTEGER, wage INTEGER, spouse INTEGER, children INTEGER, education INTEGER)'''
    c.execute(command)
    db.commit()
def addPlay(username, name, address):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("INSERT INTO plays (user_id, player_id, name, age, health, mental_health, address, alcoholism, wage, spouse, children, education) VALUES (?, ?, ?)", (getIDFromUsername(username), getnumPlaysFromUsername(username) + 1, name, 0, 0, 0, address, 0, 0, 0, 0, 0))
    db.commit()
def incrementAge(username, pid):
def changeHealth(username, pid, change):
def changeMentalHealth(username, pid, change):
def changeAddress(username, pid, newValue):
def changeAlcoholism(username, pid, newValue):
def changeWage(username, pid, newValue):
