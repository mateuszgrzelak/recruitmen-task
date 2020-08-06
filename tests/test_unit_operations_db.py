import sys
from unittest.mock import Mock
import pytest
sys.path.insert(1, '..')
from DBOperationsService import DBOperationsService
from math import isclose


class TestDBO:

    def test_percentage_women_should_be_ok_if_man_5_woman_10(self):
        repo = Mock()

        def mock_number_men_women():
            return 5, 10
        repo.get_number_men_women = mock_number_men_women
        dbo = DBOperationsService(repo)
        assert isclose(dbo.percentage_women(), 10/15*100)

    def test_percentage_men_should_be_ok_if_man_5_woman_10(self):
        repo = Mock()

        def mock_number_men_women():
            return 5, 10
        repo.get_number_men_women = mock_number_men_women
        dbo = DBOperationsService(repo)
        assert isclose(dbo.percentage_men(), 5/15*100)

    def test_average_age_female_should_return_true(self):
        repo = Mock()

        def mock_average_age_female():
            return 25.3
        repo.get_average_age_female = mock_average_age_female
        dbo = DBOperationsService(repo)
        assert isclose(dbo.average_age_female(), 25.3)

    def test_average_age_male_should_return_true(self):
        repo = Mock()

        def mock_average_age_male():
            return 44.4
        repo.get_average_age_male = mock_average_age_male
        dbo = DBOperationsService(repo)
        assert isclose(dbo.average_age_male(), 44.4)

    def test_average_age_all_should_return_true(self):
        repo = Mock()

        def mock_get_average_age_all():
            return 33.9
        repo.get_average_age_all = mock_get_average_age_all
        dbo = DBOperationsService(repo)
        assert isclose(dbo.average_age_all(), 33.9)

    def test_most_common_cities_limit_3(self):
        repo = Mock()
        cities = [('AA', 10), ('BB', 8), ('CC', 8), ('DD', 5), ('GG', 3), ('asdf', 2)]

        def mock_most_common_cities(number):
            return cities
        repo.get_most_common_cities = mock_most_common_cities
        dbo = DBOperationsService(repo)
        assert all(x in cities for x in dbo.most_common_cities(3))

    def test_most_common_cities_limit_minus_one_should_raise_exception(self):
        repo = Mock()
        cities = [('AA', 10), ('BB', 8), ('CC', 8), ('DD', 5), ('GG', 3), ('asdf', 2)]

        def mock_most_common_cities(number):
            return cities

        repo.get_most_common_cities = mock_most_common_cities
        dbo = DBOperationsService(repo)
        with pytest.raises(Exception):
            all(x in cities for x in dbo.most_common_cities(-1))

    def test_most_common_passwords_limit_3(self):
        repo = Mock()
        passwords = [('blabla', 3), ('helo123', 2), ('qweasdzxc', 2)]

        def mock_most_common_pass(number):
            return passwords
        repo.get_most_common_passwords = mock_most_common_pass
        dbo = DBOperationsService(repo)
        assert all(x in passwords for x in dbo.most_common_passwords(3))

    def test_most_common_passwords_limit_minus_one_should_raise_exception(self):
        repo = Mock()
        passwords = [('blabla', 3), ('helo123', 2), ('qweasdzxc', 2)]

        def mock_most_common_cities(number):
            return passwords

        repo.get_most_common_cities = mock_most_common_cities
        dbo = DBOperationsService(repo)
        with pytest.raises(Exception):
            all(x in passwords for x in dbo.most_common_cities(-1))

    def test_users_born_between_1930_11_22_and_1955_10_14_should_be_ok(self):
        repo = Mock()
        users = [('user1', '1939-02-09T08:57:22.462Z'),
                 ('nextuser', '1952-03-23T15:36:51.801Z'),
                 ('newuser', '1945-09-22T22:45:44.522Z')]

        def mock_users_born_between_dates(d1, d2):
            return users
        repo.get_users_born_between_dates = mock_users_born_between_dates
        dbo = DBOperationsService(repo)
        assert users == dbo.users_born_between_dates('1930-11-22', '1955-10-14')

    def test_users_born_between_1930_11_22_and_1955_10_14_change_order_arguments_should_be_ok(self):
        repo = Mock()
        users = [('user1', '1939-02-09T08:57:22.462Z'),
                 ('nextuser', '1952-03-23T15:36:51.801Z'),
                 ('newuser', '1945-09-22T22:45:44.522Z')]

        def mock_users_born_between_dates(d1, d2):
            return users
        repo.get_users_born_between_dates = mock_users_born_between_dates
        dbo = DBOperationsService(repo)
        assert users == dbo.users_born_between_dates('1955-10-14', '1930-11-22')

    def test_users_born_between_dates_invalid_date_format(self):
        repo = Mock()
        users = [('user1', '1939-02-09T08:57:22.462Z'),
                 ('nextuser', '1952-03-23T15:36:51.801Z'),
                 ('newuser', '1945-09-22T22:45:44.522Z')]

        def mock_users_born_between_dates(d1, d2):
            return users
        repo.get_users_born_between_dates = mock_users_born_between_dates
        dbo = DBOperationsService(repo)
        with pytest.raises(Exception):
            dbo.users_born_between_dates('1925.10-14', '1930-11-22')

    def test_users_born_between_dates_invalid_date_month(self):
        repo = Mock()
        users = [('user1', '1939-02-09T08:57:22.462Z'),
                 ('nextuser', '1952-03-23T15:36:51.801Z'),
                 ('newuser', '1945-09-22T22:45:44.522Z')]

        def mock_users_born_between_dates(d1, d2):
            return users
        repo.get_users_born_between_dates = mock_users_born_between_dates
        dbo = DBOperationsService(repo)
        with pytest.raises(Exception):
            dbo.users_born_between_dates('1925-13-14', '1930-11-22')

    def test_most_secure_passwords(self):
        repo = Mock()
        passwords = [('asdfg',), ('asdfg1',), ('asdfghjk',), ('asdfghjk1',), ('Asdfghjk',), ('Asdfghjk1',),
                     ('asdfghjk#',), ('asdfghjk#1',), ('Asdfghjk#',), ('Asdfghjk#1',), ('Qweadszxc@,2',)]

        def mock_all_passwords():
            return passwords

        repo.get_all_passwords = mock_all_passwords
        dbo = DBOperationsService(repo)
        assert ['Asdfghjk#1', 'Qweadszxc@,2'] == dbo.most_secure_passwords()

    def test_most_secure_passwords_should_return_false_due_to_invalid_password(self):
        repo = Mock()
        passwords = [('asdfg',), ('asdfg1',), ('asdfghjk',), ('asdfghjk1',), ('Asdfghjk',), ('Asdfghjk1',),
                     ('asdfghjk#',), ('asdfghjk#1',), ('Asdfghjk#',), ('Asdfghjk#1',), ('Qweadszxc@,2',)]

        def mock_all_passwords():
            return passwords

        repo.get_all_passwords = mock_all_passwords
        dbo = DBOperationsService(repo)
        assert ['Asdfghjk#1', 'Asdfghjk#'] != dbo.most_secure_passwords()
