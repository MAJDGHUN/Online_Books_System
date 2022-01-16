import sqlite3
#back end

#a Connection object that represents the database
#a Cursor object and call its execute() method to perform SQL commands
def ConnectData():
    con = sqlite3.connect("books.db")
    cur= con.cursor()
    #cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, BT text, BA text, BR text, BPD text, BP text, BI text, BC text)")
    cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, Book text, Author text, Rating text, Publish text, Price text, ISBN text, Bookcase text)")


    con.commit()
    con.close()
#Add Data to books DB
def addDataRec(BT,BA,BR,BPD, BP, BI, BC):
    con =sqlite3.connect("books.db")
    cur= con.cursor()
    cur.execute("INSERT INTO books VALUES (NULL,?,?,?,?,?,?,?)", \
               (BT,BA,BR,BPD,BP,BI, BC))

    con.commit()
    con.close()

#View Data From books DB
def viewData():
    con=sqlite3.connect("books.db")
    cur= con.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    con.close
    return rows

#DELETE Data From books DB
def deletRec(id):
    con=sqlite3.connect("books.db")
    cur= con.cursor()
    cur.execute("DELETE FROM books WHERE id=?", (id,))
    con.commit()
    con.close

#Search Data From books DB
def SEARCHdata(BT="",BA="",BR="",BPD="",BP="",BI="",BC=""):

    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM books WHERE Book=? OR Author=? OR Rating=? \
        OR Publish=? OR Price=? OR ISBN=? OR Bookcase=?", \
                 (BT,BA,BR,BPD, BP, BI, BC))
    rows=cur.fetchall()
    con.close()
    return rows

#Update Data to books DB
def dataupdate(id,BT="",BA="",BR="",BPD="",BP="",BI="",BC=""):
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("UPDATE books SET Book=?, Author=?, Rating=?, Publish=?, \
        Price=?, ISBN=?, Bookcase=?", \
                 (BT,BA,BR,BPD, BP, BI, BC, id))
    
    con.commit()
    con.close()
   

ConnectData()