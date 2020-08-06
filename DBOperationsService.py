import re
from datetime import datetime
from PersonRepository import PersonRepository


class DBOperationsService:

    def __init__(self, repository: 'PersonRepository'):
        self.__repository = repository

    def percentage_women(self) -> float:
        number_men, number_women = self.__repository.get_number_men_women()
        return number_women / (number_men + number_women) * 100

    def percentage_men(self) -> float:
        number_men, number_women = self.__repository.get_number_men_women()
        return number_men / (number_men + number_women) * 100

    def average_age_all(self) -> float:
        return self.__repository.get_average_age_all()

    def average_age_male(self) -> float:
        return self.__repository.get_average_age_male()

    def average_age_female(self) -> float:
        return self.__repository.get_average_age_female()

    def most_common_cities(self, limit: int) -> list:
        if limit <= 0:
            raise Exception('Limit must be grater than 0')
        return self.__repository.get_most_common_cities(limit)

    def most_common_passwords(self, limit: int) -> list:
        if limit <= 0:
            raise Exception('Limit must be grater than 0')
        return self.__repository.get_most_common_passwords(limit)

    def __replace_dates_if_in_wrong_order(self, d1: str, d2: str) -> tuple:
        t1 = datetime(int(d1[:4]), int(d1[5:7]), int(d1[8:10]))
        t2 = datetime(int(d2[:4]), int(d2[5:7]), int(d2[8:10]))
        if t1 > t2:
            return d2, d1
        return d1, d2

    def users_born_between_dates(self, d1: str, d2: str) -> list:
        """
        :param d1: # format YYYY-MM-DD
        :param d2: # format YYYY-MM-DD
        :return:
        """
        pattern = re.compile(r'^(19|20)\d\d-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])$')
        if not pattern.match(d1) or not pattern.match(d2):
            raise Exception('Invalid date format')
        d1, d2 = self.__replace_dates_if_in_wrong_order(d1, d2)
        # first date is inclusive, but the second is exclusive, i.e. d2 is equal to YYYY:MM:DD:00:00:00
        # to prevent from being out of scope added following modification
        d2 = d2 + 'T23:59:59.999Z'
        return self.__repository.get_users_born_between_dates(d1, d2)

    def __get_points_for_password(self, password: str) -> int:
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

    def most_secure_passwords(self) -> list:
        result = self.__repository.get_all_passwords()
        max_points = 0
        most_secure_passwords = []
        for res in result:
            password = res[0]
            points_for_password = self.__get_points_for_password(password)
            if points_for_password == max_points:
                most_secure_passwords.append(password)
            elif points_for_password > max_points:
                max_points = points_for_password
                most_secure_passwords = [password, ]
        return most_secure_passwords
