import sqlite3
import os
class Hiscore:
    def __init__(self):
        """Initializer for hiscore class.
            Establishes connection to sqlite database, connect cursor.
            Initializes database with default scores, if empty."""
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS scores (name text, score int)')
        self.conn.commit()
        self.cursor.execute('SELECT count(*) FROM scores')
        count = self.cursor.fetchone()[0]
        if count == 0:
            default_scores = [("topi", 4500), ("topi", 5000), ("topi", 3000),
                              ("perttu", 1200), ("erkki", 1500)]
            for score in range(5):
                name = default_scores[score][0]
                score = default_scores[score][1]
                self.cursor.execute('INSERT INTO scores VALUES (?, ?)', [name, score])
                self.conn.commit()
        self.name = os.getlogin()

    def get_highest_own(self):
        """function that returns highest score of player"""
        self.cursor.execute('SELECT score FROM scores WHERE name=? ORDER BY score DESC',
                            [self.name])
        hiscore = self.cursor.fetchone()
        return hiscore

    def get_top_five(self):
        """function that returns five highest scores"""
        self.cursor.execute('SELECT name, score FROM scores ORDER BY score DESC LIMIT 5')
        five = self.cursor.fetchall()
        return five

    def add_score(self, score):
        """add score to database
        params: score
        """
        self.cursor.execute('INSERT INTO scores VALUES (?, ?)', [self.name, score])
        self.conn.commit()

    def _close(self):
        self.conn.close()
