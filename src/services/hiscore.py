import sqlite3
class Hiscore:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.c = self.conn.cursor()
        self.c.execute('CREATE TABLE IF NOT EXISTS scores (name text, score int)')
        self.conn.commit()

    def get_hiscore(self):
        name = "topi"


        self.c.execute('SELECT 1 FROM scores WHERE name=?', [name])
        if self.c.fetchone() is None:
            self.c.execute('INSERT INTO scores VALUES (?, 0)', [name])
            self.conn.commit()
            hiscore = 0
        else:
            self.c.execute('SELECT score FROM scores WHERE name=?', [name])
            hiscore = self.c.fetchone()
        return hiscore

    def get_top_five(self):
        self.c.execute('SELECT name, score FROM scores ORDER BY score DESC LIMIT 5')
        five = self.c.fetchall()
        return five

    def add_score(self, name, score):
        self.c.execute('INSERT INTO scores VALUES (?, ?)', [name, score])
        self.conn.commit()

    def check_for_row(self, name):
        ## Set the hiscore
        hiscore = 1

        # check if row exists
        self.c.execute('SELECT 1 FROM scores WHERE name=?', [name])
        if self.c.fetchone() is None:
            self.c.execute('INSERT INTO scores VALUES (?, ?)', [name, hiscore])
        else:
            self.c.execute('UPDATE scores SET score=? WHERE name=?', [hiscore, name])

        self.conn.commit()

    def close(self):
        self.conn.close()
## Close the connection
db=Hiscore()
print(db.get_hiscore())
print(db.get_top_five())
db.close()