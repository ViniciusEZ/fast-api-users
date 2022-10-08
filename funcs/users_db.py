import sqlite3 


def db_connection(db):
    con = sqlite3.connect(db)
    return con
    
    
def select(con, _id):
    cur = con.cursor()
    selection = cur.execute(f"SELECT * FROM Users WHERE id=?", (_id,)).fetchone()
    return selection
    
    

