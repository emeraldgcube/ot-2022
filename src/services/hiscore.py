from re import S
import sqlite3
import os
class Hiscore:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.c = self.conn.cursor()
        self.c.execute('CREATE TABLE IF NOT EXISTS scores (name text, score int)')
        self.conn.commit()
        self.c.execute('SELECT count(*) FROM scores')
        count = self.c.fetchone()[0]
        if count == 0:
            default_scores = [("topi", 4500), ("topi", 5000), ("topi", 3000), ("perttu", 1200), ("erkki", 1500)]
            for score in range(5):
                print(score)
                name = default_scores[score][0]
                score = default_scores[score][1]
                self.c.execute('INSERT INTO scores VALUES (?, ?)', [name, score])
                self.conn.commit()
        self.name = os.getlogin()

    def get_highest_own(self):
        self.c.execute('SELECT score FROM scores WHERE name=? ORDER BY score DESC', [self.name])
        hiscore = self.c.fetchone()
        return hiscore

    def get_top_five(self):
        self.c.execute('SELECT name, score FROM scores ORDER BY score DESC LIMIT 5')
        five = self.c.fetchall()
        return five

    def add_score(self, score):
        self.c.execute('INSERT INTO scores VALUES (?, ?)', [self.name, score])
        self.conn.commit()
        print(self.get_highest_own())


    def close(self):
        self.conn.close()
