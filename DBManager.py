import sqlite3

class DBManager:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
    
    def close(self):
        self.conn.close()
    
    def get_all(self, table):
        self.cursor.execute(f"SELECT * FROM {table}")
        return self.cursor.fetchall()
    
    def insert(self, name, namespace, desc, version):
        self.cursor.execute("INSERT INTO datapacks (name, namespace, desc, version) VALUES (?,?,?,?)", (name, namespace, desc, version))
        self.conn.commit()
    
    def get_pack(self, pack_name):
        self.cursor.execute(f"SELECT * FROM datapacks WHERE name='{pack_name}'")
        return self.cursor.fetchall()[0]
    
    def clear_table(self, table):
        self.cursor.execute(f"DELETE FROM {table}")
        self.conn.commit()