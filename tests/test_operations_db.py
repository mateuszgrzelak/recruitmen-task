import sys
sys.path.insert(1, '..')
import DBOperationsService
import pytest


class TestDBO:
    dbo = DBOperationsService.DBOperationsService('data_test.db')

    def test_should_return_most_secure_passwords_list(self):
        passwords = self.dbo.most_secure_password()
        assert passwords == ['minemine', 'animated', 'asdfghjkl']

    def test_should_return_correct_percentage_of_men(self):
        percent_men = self.dbo.percentage_men()
        assert percent_men == 50

    def test_should_return_correct_percentage_of_women(self):
        percent_women = self.dbo.percentage_women()
        assert percent_women == 50

    def test_should_return_correct_age_of_men(self):
        aa = self.dbo.average_age_male()
        assert aa == 52.4

    def test_should_return_correct_age_of_women(self):
        aa = self.dbo.average_age_male()
        assert aa == 52.4

    def test_should_return_correct_age_of_generally(self):
        aa = self.dbo.average_age_generally()
        assert aa == 55.8

    def test_should_return_five_most_common_cities(self):
        cities = self.dbo.most_common_cities(5)
        all_cities = [('Bray', 1), ('Maynooth', 1), ('Notre Dame de Lourdes', 1), ('Salla', 1),
                      ('Churwalden', 1), ('Grenoble', 1), ('Caven', 1), ('Hagen', 1), ('Scottsdale', 1), ('Lumsden', 1)]
        assert all(x in all_cities for x in cities)

    def test_should_return_five_most_common_passwords(self):
        passwords = self.dbo.most_common_passwords(5)
        all_passwords = [('bigben', 1), ('minemine', 1), ('animated', 1), ('hall', 1),
                      ('yyyyyy', 1), ('body', 1), ('loving', 1), ('asdfghjkl', 1), ('cookie1', 1), ('julio', 1)]
        assert all(x in all_passwords for x in passwords)

    def test_should_return_users_born_between_1945_12_31_and_1955_12_31(self):
        users = self.dbo.users_born_between_dates('1945-12-31', '1955-12-31')

        assert users == [('orangewolf556','1950-05-06T08:57:22.462Z'), ('orangeelephant208','1952-02-06T15:36:51.801Z'),
                         ('heavylion807','1953-09-27T22:45:44.522Z')]

    def test_users_born_between_should_raise_exception(self):
        with pytest.raises(Exception):
            self.dbo.users_born_between_dates('1945-13-31', '1955-12-31')

    def test_should_return_most_secure_passwords(self):
        passwords = self.dbo.most_secure_password()
        assert passwords == ['minemine', 'animated', 'asdfghjkl']
