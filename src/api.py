from flask import Flask, request
import logging
import sqlite3
import json


logging.basicConfig(filename='api.log', level=logging.DEBUG)
app = Flask(__name__)


def checklogin(user, passwd):
    """Funktion, um übermittelte Logininformatioenen mit einer Hinterlegten
    Datenbank zu vergeichen. Gibt ein Tupel aus Status (0 -> erfolgreich/ 
    1 -> Fehler) und Anzeigenamen des Users (nur bei erfolgreicher 
    Authentifizierung) zurück"""
    import md5 
    pillbox = sqlite3.connect("pillbox.db")
    cursor = pillbox.cursor()
    name = cursor.execute(
        "Select name from users where login = ?; ", (user,)).fetchall()
    passhash = cursor.execute(
        "Select password from users where login = ?; ", (user,)).fetchall()
    pillbox.close()
    name = name[0][0]
    passhash = passhash[0][0]
    print name
    print passhash
    givenpasshash = md5.new()
    givenpasshash.update(passwd)
    if (passhash == givenpasshash.hexdigest()):
        print ("user authenticated!")
        return (0, name)
    else:
        print ("Login failed!")
        return (1, "")


@app.route("/report/", methods=['POST'])
#Params: error
"""Stellt ein Interface zum zentralen Sammeln von Fehlermeldungen bereit"""
def report():
    try:
        logging.ERROR("Foreign error: " + request.form["error"])
    except:
        pass
    return "0"

@app.route("/patientlist", methods=['POST'])
"""Gibt eine Liste aller Patienten mit Bild und Krankenkasse aus. 
TODO: Auslagern auf eigene Verwaltungs-API"""
# Params: user,passwd
def patientlist():
    login = checklogin(request.form["user"], request.form["passwd"])

    if login[0] == 0:

        name = login[1]
        pillbox = sqlite3.connect("pillbox.db")
        cursor = pillbox.cursor()

        results = cursor.execute("select * from config").fetchall()

        pillbox.close()

        return str(results)
    else:
        return "1"

@app.route("/check", methods=['POST'])
"""Ließt die aktuelle"""
def check():
    login = checklogin(request.form["user"], request.form["passwd"])

    if login[0] == 0:

        name = login[1]
        pillbox = sqlite3.connect("pillbox.db")
        cursor = pillbox.cursor()

        results = cursor.execute("select * from config").fetchall()

        pillbox.close()

        return str(results)
    else:
        return "1"



@app.route("/instant", methods=['POST'])
# Params: user,passwd,pill,count (default 1)
def instant():
    login = checklogin(request.form["user"], request.form["passwd"])
    if login[0] == 0:
        try:
            count = request.form["count"]
        except KeyError, e:
            count = 1
        # TODO control.py anbinden
    else:
        return "1"


@app.route('/write', methods=['POST'])
def write():
    pillbox = sqlite3.connect("pillbox.db")
    cursor = pillbox.cursor()
    print (request.form["user"])
    login = checklogin(request.form["user"], request.form["passwd"])
    name = login[1]
    # try:

    query = json.loads(request.form["query"])

    if (login[0] == 0):
        cursor.execute("Delete from config where doctor = ?;", (name,))

        for hour, dosis in query:
            command = (hour, dosis, login[1])
            print command
            cursor.execute("INSERT INTO config VALUES(?,?,?)", command)
        pillbox.close()
        return "0"
    else:
        return "1"


@app.route("/")
def ping():
    test = open("post.html", "r")
    return test.read()


@app.route("/checki")
def checki():
    test = open("check.html", "r")
    return test.read()

if __name__ == "__main__":
    print "App running!"
    app.run(port=80, debug=True, host="0.0.0.0")
