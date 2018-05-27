import sqlite3

    
def create_table(table_name):
    db = sqlite3.connect('database.db')
    csr = db.cursor()
    
    csr.execute("CREATE TABLE IF NOT EXISTS " + table_name + ''' \
                                    (ID INTEGER PRIMARY KEY, 
                                     Date TEXT, 
                                     Description TEXT, 
                                     Dr REAL, 
                                     Cr REAL);
                ''')
    db.commit()
    db.close()


def drop_table(table_name):
    db = sqlite3.connect('database.db')
    csr = db.cursor()
    
    csr.execute("DROP TABLE IF EXISTS " + table_name + ";")
    
    db.commit()
    db.close()
    
    
def add_transaction(table_name, id, date, des, dr, cr):
    db = sqlite3.connect('database.db')
    csr = db.cursor()
    
    csr.execute("INSERT INTO " + table_name + \
                    '''(ID, Date, Description, Dr, Cr)
                        VALUES(?,?,?,?,?)''', (id, date, des, dr, cr))
    
    print('new transaction inserted')
 
    db.commit()
    db.close()
    
    
def display_table(pd, table_name):
    db = sqlite3.connect('database.db')
    
    table  = pd.read_sql_query("SELECT * from " + table_name, db)
    
    db.commit()
    db.close()
    
    return table