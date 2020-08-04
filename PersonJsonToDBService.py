import sqlite3
import calendar
import json
from datetime import datetime
import requests


class PersonJsonToDBService:

    def __init__(self, db_name='data.db'):
        self.__conn = sqlite3.connect(db_name)
        self.__c = self.__conn.cursor()

    def __create_tables(self):
        self.__c.execute('''CREATE TABLE IF NOT EXISTS person
                     (id integer PRIMARY KEY,
                      gender text NOT NULL,
                      email text NOT NULL,
                      phone text NOT NULL,
                      cell text NOT NULL,
                      nat text NOT NULL,
                      daysToBirthday integer NOT NULL
                        )''')
        self.__c.execute('''CREATE TABLE IF NOT EXISTS personName
                     (id integer PRIMARY KEY,
                      title text,
                      first text,
                      last text
                     )''')
        self.__c.execute('''CREATE TABLE IF NOT EXISTS personLocation
                     (id integer PRIMARY KEY,
                      city text,
                      state text,
                      country text,
                      postcode text
                     )''')
        self.__c.execute('''CREATE TABLE IF NOT EXISTS personLocationStreet
                     (
                      id integer PRIMARY KEY,
                      number text,
                      name text
                     )''')
        self.__c.execute('''CREATE TABLE IF NOT EXISTS personLocationCoordinates
                     (
                      id integer PRIMARY KEY,
                      latitude text,
                      longitude text
                     )''')
        self.__c.execute('''CREATE TABLE IF NOT EXISTS personLocationTimezone
                     (
                      id integer PRIMARY KEY,
                      offset text,
                      description text
                     )''')
        self.__c.execute('''CREATE TABLE IF NOT EXISTS personLogin
                     (
                      id integer PRIMARY KEY,
                      uuid text,
                      username text,
                      password text,
                      salt text,
                      md5 text,
                      sha1 text,
                      sha256 text
                     )''')
        self.__c.execute('''CREATE TABLE IF NOT EXISTS personDOB
                     (
                      id integer PRIMARY KEY,
                      date text,
                      age integer
                     )''')
        self.__c.execute('''CREATE TABLE IF NOT EXISTS personRegistered
                     (
                      id integer PRIMARY KEY,
                      date text,
                      age integer
                     )''')
        self.__c.execute('''CREATE TABLE IF NOT EXISTS personId
                     (
                      id integer PRIMARY KEY,
                      name text,
                      value text
                     )''')
        self.__conn.commit()

    def __days_to_birthday(self, month: int, day: int):
        day_buff = day
        if not calendar.isleap(datetime.now().year) and month == 2 and day_buff == 29:
            day = 28
        delta1 = datetime(datetime.now().year, month, day)
        bd_this_year = (delta1 - datetime.now()).days
        if bd_this_year >= -1:
            return bd_this_year + 1
        if not calendar.isleap(datetime.now().year + 1) and month == 2 and day_buff == 29:
            day = 28
        delta2 = datetime(datetime.now().year + 1, month, day)
        bd_next_year = (delta2 - datetime.now()).days
        return bd_next_year + 1

    def __clean_phone_number_from_special_character(self, phone_number: str):
        return ''.join(e for e in phone_number if e.isnumeric())

    def __insert_data_to_tables(self, number):
        json_data = requests.get('https://randomuser.me/api/?results='+str(number)).text
        data = json.loads(json_data)
        for d in data['results']:
            date_of_birth = d['dob']['date'][:10]  # Format 2016-08-11
            dtb = self.__days_to_birthday(int(date_of_birth[5:7]), int(date_of_birth[8:10]))
            phone_number = self.__clean_phone_number_from_special_character(d['phone'])
            self.__c.execute('''
            INSERT INTO person(gender,email,phone,cell,nat,daysToBirthday)
            VALUES(?,?,?,?,?,?)
            ''', (d['gender'], d['email'], phone_number, d['cell'], d['nat'], dtb))
            self.__c.execute('''
            INSERT INTO personName(title, first, last)
            VALUES(?,?,?)
            ''', (d['name']['title'], d['name']['first'], d['name']['last']))
            self.__c.execute('''
            INSERT INTO personLocation(city, state, country, postcode)
            VALUES(?,?,?,?)
            ''', (
                d['location']['city'], d['location']['state'],
                d['location']['country'], d['location']['postcode'])
                             )
            self.__c.execute('''
            INSERT INTO personLocationStreet(number, name)
            VALUES(?,?)
            ''', (d['location']['street']['number'], d['location']['street']['name']))
            self.__c.execute('''
            INSERT INTO personLocationCoordinates(latitude, longitude)
            VALUES(?,?)
            ''', (d['location']['coordinates']['latitude'], d['location']['coordinates']['longitude']))
            self.__c.execute('''
            INSERT INTO personLocationTimezone(offset, description)
            VALUES(?,?)
            ''', (d['location']['timezone']['offset'], d['location']['timezone']['description']))
            self.__c.execute('''
            INSERT INTO personLogin(uuid, username, password, salt, md5, sha1, sha256)
            VALUES(?,?,?,?,?,?,?)
            ''', (
                d['login']['uuid'], d['login']['username'], d['login']['password'], d['login']['salt'],
                d['login']['md5'],
                d['login']['sha1'], d['login']['sha256']))
            self.__c.execute('''
            INSERT INTO personDOB(date, age)
            VALUES(?,?)
            ''', (d['dob']['date'], d['dob']['age']))
            self.__c.execute('''
            INSERT INTO personRegistered(date, age)
            VALUES(?,?)
            ''', (d['registered']['date'], d['registered']['age']))
            self.__c.execute('''
            INSERT INTO personId(name, value)
            VALUES(?,?)
            ''', (d['id']['name'], d['id']['value']))
            self.__conn.commit()

    def convert_to_database(self, number_persons):
        '''
        :param number_persons: number of persons taken from external api
        :return:
        '''
        self.__create_tables()
        self.__insert_data_to_tables(number_persons)
        self.__close_connection()

    def __close_connection(self):
        self.__conn.close()
