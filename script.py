import click
import PersonJsonToDBService
import DBOperationsService


@click.command()
@click.option('--load-to-db', '-ltdb', 'ltdb', type=int,
              help='Create .db file from json file. The argument specifies how '
                   'many people should be created in database.')
@click.option('--percentage', '-p', 'p',
              type=click.Choice(['male', 'female'], case_sensitive=False),
              help='Get percentage of men or women.')
@click.option('--average-age', '-aa', 'aa',
              type=click.Choice(['male', 'female', 'generally'], case_sensitive=False),
              help='Get average age of men, women or men+women.')
@click.option('--most-common-cities', '-mcc', 'mcc', type=int,
              help='Get [number] most common cities.')
@click.option('--most-common-pass', '-mcp', 'mcp', type=int,
              help='Get [number] most common passwords.')
@click.option('--users-born-between-dates', '-ubbd', 'ubbd', nargs=2,
              help='Get all users born between first and second argument. '
                   'Arguments should be in format YYYY-MM-DD.')
@click.option('--most-secure-pass', '-msp', 'msp', is_flag=True,
              help='Get the most secure passwords using a specific ranking.')
def hello(ltdb, p, aa, mcc, mcp, ubbd, msp):
    '''
    My solution of the recruitment task.
    People data is taken from external api https://randomuser.me/.
    First you need to create db using argument -ltdb [number of people taken].
    Then you can perform the operations listed below. In folder where project is located data.db file will be created
    '''
    if ltdb is not None:
        load_to_db(ltdb)
    if p is not None:
        percentage(p)
    if aa is not None:
        average_age(aa)
    if mcc is not None:
        most_common_cities(mcc)
    if mcp is not None:
        most_common_pass(mcp)
    if len(ubbd) == 2:
        users_born_between_dates(ubbd[0], ubbd[1])
    if msp:
        most_secure_pass()


def load_to_db(number: int):
    pjtdb = PersonJsonToDBService.PersonJsonToDBService()
    pjtdb.convert_to_database(number)
    print('Converted data from .json to .db format.\nCreated '
          'tables with data about '+str(number)+' persons')


def percentage(gender: str):
    service = DBOperationsService.DBOperationsService()
    if gender == 'male':
        print('Percentage of men: '+str(service.percentage_men())+'%')
    elif gender == 'female':
        print('Percentage of women: '+str(service.percentage_women())+'%')
    service.close_connection()


def average_age(gender: str):
    service = DBOperationsService.DBOperationsService()
    if gender == 'male':
        print('The average age of men: ' + str(service.average_age_male()))
    elif gender == 'female':
        print('The average age of women: ' + str(service.average_age_female()))
    elif gender == 'generally':
        print('The average age of men and women: ' + str(service.average_age_generally()))
    service.close_connection()


def most_common_cities(limit: int):
    service = DBOperationsService.DBOperationsService()
    print(str(limit)+' most popular cities: ')
    for city, occurrence in service.most_common_cities(limit):
        print('City: ' + city+', occurrences: '+str(occurrence))
    service.close_connection()


def most_common_pass(limit: int):
    service = DBOperationsService.DBOperationsService()
    print(str(limit)+' most popular passwords:')
    for password, occurrence in service.most_common_passwords(limit):
        print('Password: ' + password + ', occurrences: ' + str(occurrence))
    service.close_connection()


def users_born_between_dates(d1: str, d2: str):
    service = DBOperationsService.DBOperationsService()
    print('Users born between '+d1+' and '+d2+':')
    for username in service.users_born_between_dates(d1, d2):
        print(username[0])
    service.close_connection()


def most_secure_pass():
    service = DBOperationsService.DBOperationsService()
    print('The most secure passwords:')
    for password in service.most_secure_password():
        print(password)
    service.close_connection()


if __name__ == '__main__':
    hello()
