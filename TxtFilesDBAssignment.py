
import sqlite3

conn = sqlite3.connect('test2.db')

with conn:
    cur = conn.cursor()
    # create table with an auto-increment integer field and a text field
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_txtfiles( \
    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    col_filename TEXT \
    )")
    conn.commit()
conn.close()


conn = sqlite3.connect('test2.db')

# create tuple of files for program to read through
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# loop through each object in the tuple to find the file names that end in .txt
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            # the value for each row will be one name out of the tuple therefore (x,)
            # will denote a one-element list for each name ending with y
            cur.execute("INSERT INTO tbl_txtfiles (col_filename) VALUES (?)", (x,))
            conn.commit()
conn.close()


conn = sqlite3.connect('test2.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT ALL col_filename FROM tbl_txtfiles")
    varFiles = cur.fetchall()
    for item in varFiles:
        msg = "File Name: {}".format(item[0])
        print(msg)
conn.close()
        
