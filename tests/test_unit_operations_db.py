import sys
from unittest.mock import Mock
sys.path.insert(1, '..')
from DBOperationsService import DBOperationsService
import PersonRepository
from unittest.mock import Mock


class TestDBO:

    def test_get_number_men_women(self):
        repo = Mock()

        def mock_get_number_men_women():
            return 10, 10
        repo.get_number_men_women = mock_get_number_men_women
        dbo = DBOperationsService(repo)
        assert dbo.percentage_women() == 50


    # def get_average_age_all(self) -> float:
    #     return 30
    #
    # def get_average_age_male(self) -> float:
    #     return 20
    #
    # def get_average_age_female(self) -> float:
    #     return 40.0
    #
    # def get_most_common_cities(self, limit: int) -> list:
    #     self.__cur.execute('SELECT city, COUNT(city) as cnt FROM personLocation'
    #                        ' GROUP BY city order by cnt desc LIMIT ' + str(limit))
    #     return self.__cur.fetchall()
    #
    # def get_most_common_passwords(self, limit: int) -> list:
    #     self.__cur.execute('SELECT password, COUNT(password) as cnt FROM personLogin'
    #                        ' GROUP BY password order by cnt desc LIMIT ' + str(limit))
    #     return self.__cur.fetchall()
    #
    # def get_users_born_between_dates(self, d1: str, d2: str) -> list:
    #     self.__cur.execute("SELECT username, date FROM personLogin, personDOB WHERE personDOB.date >= '" + d1 + "'"
    #                        " and personDOB.date <= '" + d2 + "'and personDOB.id = personLogin.id")
    #     return self.__cur.fetchall()
    #
    # def get_all_passwords(self) -> list:
    #     self.__cur.execute('SELECT password FROM personLogin')
    #     return self.__cur.fetchall()
    #
    # def close_connection(self):
    #     self.__conn.close()
