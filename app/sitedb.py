# GiraffeSnakeOtterPenguin: Stella, Moyo, Evan, Jady
# SoftDev
# April 2024

import sqlite3

DB_FILE="app/databse.db"

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
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    if (c.execute("SELECT 1 FROM users WHERE username=?", (username,))).fetchone() == None:
        return
    c.execute("UPDATE users SET score=? WHERE username=?", (score, username))
    db.commit()
def incrementnumPlays(username):
    db = sqlite3.connect(DB_FILE)
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
    c.execute("SELECT username FROM users WHERE username=?", (username,))
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
    c.execute("SELECT username FROM users WHERE user_id=?", (uid,))
    c.fetchone()[0]
def getIDFromUsername(username):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT user_id FROM users WHERE username=?", (username,))
    return c.fetchone()[0]
def getScoreFromID(uid):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT score FROM users WHERE user_id=?", (uid,))
    return c.fetchone()[0]
def getScoreFromUsername(username):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT score FROM users WHERE username=?", (username,))
    return c.fetchone()[0]
def getnumPlaysFromUsername(username):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT numPlays FROM users WHERE username=?", (username,))
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
    command = '''CREATE TABLE IF NOT EXISTS plays (user_id INTEGER, play_id INTEGER, name TEXT, age INTEGER, health INTEGER,
                mental_health INTEGER, address TEXT,
                alcoholism INTEGER, wage INTEGER, spouse INTEGER, children INTEGER, education INTEGER)'''
    c.execute(command)
    db.commit()
def addPlay(username, name, address):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("INSERT INTO plays (user_id, play_id, name, age, health, mental_health, address, alcoholism, wage, spouse, children, education) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (getIDFromUsername(username), getnumPlaysFromUsername(username) + 1, name, 0, 0, 0, address, 0, 0, 0, 0, 0))
    db.commit()
    incrementnumPlays(username)
    db.commit()

def incrementAge(username, pid):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    if (c.execute("SELECT 1 FROM plays WHERE user_id=? AND play_id=?", (getIDFromUsername(username), pid))).fetchone() == None:
        return
    curr = getAge(username, pid) + 1
    c.execute("UPDATE plays SET age=? WHERE user_id=? AND play_id=?", (curr + 1, getIDFromUsername(username), pid))
    db.commit()
def changeHealth(username, pid, change):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    if (c.execute("SELECT 1 FROM plays WHERE user_id=? AND play_id=?", (getIDFromUsername(username), pid))).fetchone() == None:
        return
    c.execute("UPDATE plays SET health=? WHERE user_id=? AND play_id=?", (getHealth(username, pid) + change, getIDFromUsername(username), pid, ))
    db.commit()
def changeMentalHealth(username, pid, change):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    if (c.execute("SELECT 1 FROM plays WHERE user_id=? AND play_id=?", (getIDFromUsername(username), pid))).fetchone() == None:
        return
    c.execute("UPDATE plays SET mental_health=? WHERE user_id=? AND play_id=?", (getAge(username, pid) + 1, getIDFromUsername(username), pid, ))
    db.commit()
def changeAddress(username, pid, newValue):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    if (c.execute("SELECT 1 FROM plays WHERE user_id=? AND play_id=?", (getIDFromUsername(username), pid))).fetchone() == None:
        return
    c.execute("UPDATE plays SET mental_health=? WHERE user_id=? AND play_id=?", (newValue, getIDFromUsername(username), pid, ))
    db.commit()
def changeAlcoholism(username, pid, newValue):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    if (c.execute("SELECT 1 FROM plays WHERE user_id=? AND play_id=?", (getIDFromUsername(username), pid))).fetchone() == None:
        return
    c.execute("UPDATE plays SET alcoholism=? WHERE user_id=? AND play_id=?", (newValue, getIDFromUsername(username), pid, ))
    db.commit()
def changeWage(username, pid, newValue):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    if (c.execute("SELECT 1 FROM plays WHERE user_id=? AND play_id=?", (getIDFromUsername(username), pid))).fetchone() == None:
        return
    c.execute("UPDATE plays SET wage=? WHERE user_id=? AND play_id=?", (newValue, getIDFromUsername(username), pid))
    db.commit()
def changeMaritialStatus(username, pid):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    if (c.execute("SELECT 1 FROM plays WHERE user_id=? AND play_id=?", (getIDFromUsername(username), pid))).fetchone() == None:
        return
    c.execute("UPDATE plays SET spouse=? WHERE user_id=? AND play_id=?", ((getMaritialStatus(username, pid) + 1)%2, getIDFromUsername(username), pid, ))
    db.commit()
def changeChildCount(username, pid, change):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    if (c.execute("SELECT 1 FROM plays WHERE user_id=? AND play_id=?", (getIDFromUsername(username), pid))).fetchone() == None:
        return
    c.execute("UPDATE plays SET children=? WHERE user_id=? AND play_id=?", ( getChildCount(username, pid) + change, getIDFromUsername(username), pid,))
    db.commit()
def incrementEdu(username, pid):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    if (c.execute("SELECT 1 FROM plays WHERE user_id=? AND play_id=?", (getIDFromUsername(username), pid))).fetchone() == None:
        return
    c.execute("UPDATE plays SET education=? WHERE user_id=? AND play_id=?", (getEducation(username, pid) + 1, getIDFromUsername(username), pid, ))
    db.commit()

#accessor functions
def getName(username, pid):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT name FROM plays WHERE user_id=? AND play_id=?", (getIDFromUsername(username), pid))
    return c.fetchone()[0]
def getAge(username, pid):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT age FROM plays WHERE user_id=? AND play_id=?", (getIDFromUsername(username), pid))
    return c.fetchone()[0]
def getHealth(username, pid):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT health FROM plays WHERE user_id=? AND play_id=?", (getIDFromUsername(username), pid))
    return c.fetchone()[0]
def getMentalHealth(username, pid):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT mental_health FROM plays WHERE user_id=? AND play_id=?", (getIDFromUsername(username), pid))
    return c.fetchone()[0]
def getAddress(username, pid):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT address FROM plays WHERE user_id=? AND play_id=?", (getIDFromUsername(username), pid))
    return c.fetchone()[0]
def getAlcoholism(username, pid):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT alcoholism FROM plays WHERE user_id=? AND play_id=?", (getIDFromUsername(username), pid))
    return c.fetchone()[0]
def getWage(username, pid):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT wage FROM plays WHERE user_id=? AND play_id=?", (getIDFromUsername(username), pid))
    return c.fetchone()[0]
def getMaritialStatus(username, pid):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT spouse FROM plays WHERE user_id=? AND play_id=?", (getIDFromUsername(username), pid))
    return c.fetchone()[0]
def MaritialStatusToString(username, pid):
    status = getMaritialStatus(username, pid)
    if status == None:
        return
    else:
        if status == 0:
            return "Single"
        else:
            return "Married"
def getChildCount(username, pid):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT children FROM plays WHERE user_id=? AND play_id=?", (getIDFromUsername(username), pid))
    return c.fetchone()[0]
def getEducation(username, pid):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT education FROM plays WHERE user_id=? AND play_id=?", (getIDFromUsername(username), pid))
    return c.fetchone()[0]
def EducationStatusToString(username, pid):
    status = getEducation(username, pid)
    if status == None:
        return
    else:
        stat = status
        if stat  == 0:
            return "Uneducated"
        elif stat == 1:
            return "Elementary School"
        elif stat == 2:
            return "Middle School"
        elif stat == 3:
            return "High School"
        elif stat == 4:
            return "College"
        elif stat == 5:
            return "Post-Grad"
# return game information
def getGamesInfo(uid):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT * FROM plays WHERE user_id=?", (uid,))
    return c.fetchall()
def gamesInfoToTable(games):
    i = 0
    output = "<table>"
    output += "<tr> <th>Play Number</th> <th>Name</th> <th>Age</th> <th>Address</th> <th>Alcoholism</th> <th>Wage</th> <th>Married</th> <th>Children</th> <th>Education</th></tr>"
    if len(games) > 0:
        while len(games[i]) != 0:
            output += "<tr>"
            output += "<td>" + games[i][1] + "</td>" # play num
            output += "<td>" + games[i][3] + "</td>" # name
            output += "<td>" + games[i][4] + "</td>" # age
            output += "<td>" + games[i][7] + "</td>" # address
            output += "<td>" + games[i][8] + "</td>" # alcoholism
            output += "<td>" + games[i][9] + "</td>" # wage
            output += "<td>" + MaritialStatusToString(games[i][0], games[i][1]) + "</td>" # spouse
            output += "<td>" + games[i][11] + "</td>" # children
            output += "<td>" + EducationStatusToString(games[i][0], games[i][1]) + "</td>" # education
            output += "</tr>"
            i += 1
    output += "</table>"
    return output
