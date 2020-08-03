import sqlite3


def get_points_for_password(password):
    special_characters = [" ", "!", "\"", "#", "$", "%", "&", "\'", "(", ")", "*", "+",
                          ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[",
                          "\\", "]", "^", "_", "`", "{", "|", "}", "~"]
    points = 0
    one_lower_letter = False
    one_capital_letter = False
    one_digit = False
    special_char = False
    for ch in password:
        if not one_lower_letter and ch.islower():
            points += 1
            one_lower_letter = True
        elif not one_capital_letter and ch.isupper():
            points += 2
            one_capital_letter = True
        elif not one_digit and ch.isdigit():
            points += 1
            one_digit = True
        elif not special_char and ch in special_characters:
            points += 3
            special_char = True
    if len(password) >= 8:
        points += 5
    return points


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

    def most_common_passwords(self, limit: int):
        self.cur.execute('SELECT password, COUNT(password) as cnt FROM personLogin'
                         ' GROUP BY password order by cnt desc LIMIT ' + str(limit))
        result = self.cur.fetchall()
        print(str(limit) + ' najpopularniejszych hasel:')
        for res in result:
            print(res[0] + ': ' + str(res[1]))

        # d1 and d2 format is YYYY-MM-DD
    def users_born_between_dates(self, d1, d2):
        # first date is inclusive, but the second is exclusive, i.e. d2 is equal YYYY:MM:DD:00:00:00
        # to prevent from being out of scope added following modification
        d2buff = d2 + 'T23:59:59.999Z'
        self.cur.execute("SELECT username FROM personLogin, personDOB WHERE personDOB.date >= '" + d1 + "'"
                        " and personDOB.date <= '" + d2buff + "'and personDOB.id = personLogin.id")
        result = self.cur.fetchall()
        print('Uzytkownicy urodzeni pomiędzy ' + d1 + ' oraz ' + d2 + ': ')
        for res in result:
            print(res[0])

    def most_secure_password(self):
        self.cur.execute('SELECT password FROM personLogin')
        result = self.cur.fetchall()
        max_points = 0
        most_secure_passwords = []
        for res in result:
            password = res[0]
            points_for_password = get_points_for_password(password)
            if points_for_password == max_points:
                most_secure_passwords.append(password)
            elif points_for_password > max_points:
                max_points = points_for_password
                most_secure_passwords = [password, ]

        print('Hasla ktore zdobyly najwiecej punktow za bezpieczenstwo:')
        print(most_secure_passwords)

    def close_connection(self):
        self.conn.close()
