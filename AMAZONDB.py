import sqlite3

#a Connection object that represents the database
#a Cursor object and call its execute() method to perform SQL commands
def ConnectData():
    con = sqlite3.connect("Amazonbooks.db")
    cur= con.cursor()


    con.commit()
    con.close()

#View Data From Amazonbooks DB
def viewData():
    con=sqlite3.connect("Amazonbooks.db")
    cur= con.cursor()
    cur.execute("SELECT * FROM Amazonbooks")
    rows = cur.fetchall()
    con.close
    return rows

ConnectData()

