import sqlite3


class DBOperationsService:

    def __init__(self, db_name='data.db'):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()

    def percentage_of_women(self):
        self.cur.execute('SELECT COUNT(*) FROM person WHERE gender="male"')
        number_man = self.cur.fetchall()[0][0]
        self.cur.execute('SELECT COUNT(*) FROM person WHERE gender="female"')
        number_woman = self.cur.fetchall()[0][0]
        print('Procent kobiet = ' + str(number_woman / (number_man + number_woman) * 100) + '%')

    def percentage_of_man(self):
        self.cur.execute('SELECT COUNT(*) FROM person WHERE gender="male"')
        number_man = self.cur.fetchall()[0][0]
        self.cur.execute('SELECT COUNT(*) FROM person WHERE gender="female"')
        number_woman = self.cur.fetchall()[0][0]
        print('Procent mezczyzn = ' + str(number_man / (number_man + number_woman) * 100) + '%')
