import sqlite3


class PersonRepository:

    def __init__(self, db_name='data.db'):
        self.__conn = sqlite3.connect(db_name)
        self.__cur = self.__conn.cursor()

    def get_number_men_women(self) -> (int, int):
        self.__cur.execute('SELECT COUNT(*) FROM person WHERE gender="male"')
        number_men = self.__cur.fetchall()[0][0]
        self.__cur.execute('SELECT COUNT(*) FROM person WHERE gender="female"')
        number_women = self.__cur.fetchall()[0][0]
        return number_men, number_women

    def get_average_age_all(self) -> int:
        self.__cur.execute('SELECT AVG(age) FROM personDOB')
        return self.__cur.fetchall()[0][0]

    def get_average_age_male(self) -> int:
        self.__cur.execute('SELECT AVG(age) FROM personDOB,'
                           ' person WHERE person.gender="male" AND person.id=personDOB.id')
        return self.__cur.fetchall()[0][0]

    def get_average_age_female(self) -> int:
        self.__cur.execute('SELECT AVG(age) FROM personDOB,'
                           ' person WHERE person.gender="female" AND person.id=personDOB.id')
        return self.__cur.fetchall()[0][0]

    def get_most_common_cities(self, limit: int) -> list:
        self.__cur.execute('SELECT city, COUNT(city) as cnt FROM personLocation'
                           ' GROUP BY city order by cnt desc LIMIT ' + str(limit))
        return self.__cur.fetchall()

    def get_most_common_passwords(self, limit: int) -> list:
        self.__cur.execute('SELECT password, COUNT(password) as cnt FROM personLogin'
                           ' GROUP BY password order by cnt desc LIMIT ' + str(limit))
        return self.__cur.fetchall()

    def get_users_born_between_dates(self, d1: str, d2: str) -> list:
        self.__cur.execute("SELECT username, date FROM personLogin, personDOB WHERE personDOB.date >= '" + d1 + "'"
                           " and personDOB.date <= '" + d2 + "'and personDOB.id = personLogin.id")
        return self.__cur.fetchall()

    def get_all_passwords(self):
        self.__cur.execute('SELECT password FROM personLogin')
        return self.__cur.fetchall()

    def close_connection(self):
        self.__conn.close()
