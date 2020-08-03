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

    def average_age(self):
        self.cur.execute('SELECT AVG(age) FROM personDOB')
        average_age_overall = self.cur.fetchall()[0][0]
        print('Ogolna srednia wieku: ' + str(int(average_age_overall)))

    def average_age_male(self):
        self.cur.execute('SELECT AVG(age) FROM personDOB,'
                         ' person WHERE person.gender="male" AND person.id=personDOB.id')
        average_age_man = self.cur.fetchall()[0][0]
        print('Srednia wieku mezczyzn: ' + str(int(average_age_man)))

    def average_age_female(self):
        self.cur.execute('SELECT AVG(age) FROM personDOB,'
                         ' person WHERE person.gender="female" AND person.id=personDOB.id')
        average_age_woman = self.cur.fetchall()[0][0]
        print('Srednia wieku kobiet: ' + str(int(average_age_woman)))

    def most_popular_cities(self, limit: int):
        self.cur.execute('SELECT city, COUNT(city) as cnt FROM personLocation'
                         ' GROUP BY city order by cnt desc LIMIT ' + str(limit))
        result = self.cur.fetchall()
        print(str(limit) + ' najpopularniejszych miast:')
        for res in result:
            print(res[0] + ': ' + str(res[1]))
