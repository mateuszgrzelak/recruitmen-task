import click
import DBOperationsService
import PersonRepository
import os


@click.command()
@click.option('--load-random-users', '-lru', 'lru', type=int,
              help='Create .db file. The argument specifies how '
                   'many data about people should be created in database.')
@click.option('--gender-percentage', '-gp', 'gp',
              type=click.Choice(['male', 'female'], case_sensitive=False),
              help='Get percentage of men or women.')
@click.option('--average-age', '-aa', 'aa',
              type=click.Choice(['male', 'female', 'all'], case_sensitive=False),
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
def hello(lru, gp, aa, mcc, mcp, ubbd, msp):
    '''
    My solution of the recruitment task.
    People data is taken from external api https://randomuser.me/.
    First you need to create db using argument -lru [number of people taken]. As a result data.db file will be created
    in project folder. Then you can perform the operations listed below.
    '''
    if lru is not None:
        load_random_users(lru)
    elif gp is not None:
        gender_percentage(gp)
    elif aa is not None:
        average_age(aa)
    elif mcc is not None:
        most_common_cities(mcc)
    elif mcp is not None:
        most_common_pass(mcp)
    elif len(ubbd) == 2:
        users_born_between_dates(ubbd[0], ubbd[1])
    elif msp:
        most_secure_pass()


def load_random_users(number: int):
    repository = PersonRepository.PersonRepository()
    if number < 0:
        print('Argument must be greater than 0')
        return
    repository.create_data(number)
    print('Converted data from .json to .db format.\nCreated '
          'tables with data about '+str(number)+' persons')
    repository.close_connection()


def gender_percentage(gender: str):
    if not os.path.isfile('./data.db'):
        print("Error: data.db file doesn't exist. Use --load-random-users [number] to create database.")
        return
    repository = PersonRepository.PersonRepository()
    service = DBOperationsService.DBOperationsService(repository)
    if gender == 'male':
        print('Percentage of men: '+str(round(service.percentage_men(), 1))+'%')
    elif gender == 'female':
        print('Percentage of women: '+str(round(service.percentage_women(), 1))+'%')
    repository.close_connection()


def average_age(gender: str):
    if not os.path.isfile('./data.db'):
        print("Error: data.db file doesn't exist. Use --load-random-users [number] to create database.")
        return
    repository = PersonRepository.PersonRepository()
    service = DBOperationsService.DBOperationsService(repository)
    if gender == 'male':
        print('The average age of men: ' + str(round(service.average_age_male(), 1)))
    elif gender == 'female':
        print('The average age of women: ' + str(round(service.average_age_female(), 1)))
    elif gender == 'all':
        print('The average age of men and women: ' + str(round(service.average_age_all(), 1)))
    repository.close_connection()


def most_common_cities(limit: int):
    if not os.path.isfile('./data.db'):
        print("Error: data.db file doesn't exist. Use --load-random-users [number] to create database.")
        return
    repository = PersonRepository.PersonRepository()
    service = DBOperationsService.DBOperationsService(repository)
    try:
        cities = service.most_common_cities(limit)
    except:
        print("Error: argument must be greater than 0.")
        return
    print('\n'+str(limit)+' most popular cities: \n')
    print('NAME{:>16} OCCURRENCES'.format('|'))
    print('-'*32)
    for city, occurrence in cities:
        print('{:19}| {:^11}'.format(city, str(occurrence)))
    repository.close_connection()


def most_common_pass(limit: int):
    if not os.path.isfile('./data.db'):
        print("Error: data.db file doesn't exist. Use --load-random-users [number] to create database.")
        return
    repository = PersonRepository.PersonRepository()
    service = DBOperationsService.DBOperationsService(repository)
    try:
        passwords = service.most_common_passwords(limit)
    except:
        print("Error: argument must be greater than 0.")
        return
    print('\n'+str(limit) + ' most popular passwords: \n')
    print('PASSWORD{:>12} OCCURRENCES'.format('|'))
    print('-' * 32)
    for password, occurrence in passwords:
        print('{:19}| {:^11}'.format(password, str(occurrence)))
    repository.close_connection()


def users_born_between_dates(d1: str, d2: str):
    if not os.path.isfile('./data.db'):
        print("Error: data.db file doesn't exist. Use --load-random-users [number] to create database.")
        return
    repository = PersonRepository.PersonRepository()
    service = DBOperationsService.DBOperationsService(repository)
    try:
        users = service.users_born_between_dates(d1, d2)
    except:
        print("Error: Invalid date format")
        return
    print('\nUsers born between '+d1+' and '+d2+':\n')
    print('USERNAME{:>16} DATE OF BIRTH'.format('|'))
    print('-' * 38)
    for username, dob in users:
        print('{:23}| {:^13}'.format(username, dob[:10]))
    repository.close_connection()


def most_secure_pass():
    if not os.path.isfile('./data.db'):
        print("Error: data.db file doesn't exist. Use --load-random-users [number] to create database.")
        return
    repository = PersonRepository.PersonRepository()
    service = DBOperationsService.DBOperationsService(repository)
    print('\nThe most secure passwords:\n')
    for password in service.most_secure_passwords():
        print(password)
    repository.close_connection()


if __name__ == '__main__':
    hello()
