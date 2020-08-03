import sqlite3
import calendar
from datetime import datetime


def days_to_birthday(month: int, day: int):
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


def clean_phone_number_from_special_character(phone_number: str):
    return ''.join(e for e in phone_number if e.isnumeric())


class PersonJsonToDBService:

    def __init__(self, db_name='data.db'):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()

    def create_tables(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS person
                     (id integer PRIMARY KEY,
                      gender text NOT NULL,
                      email text NOT NULL,
                      phone text NOT NULL,
                      cell text NOT NULL,
                      nat text NOT NULL,
                      daysToBirthday integer NOT NULL
                        )''')
        self.c.execute('''CREATE TABLE IF NOT EXISTS personName
                     (id integer PRIMARY KEY,
                      title text,
                      first text,
                      last text
                     )''')
        self.c.execute('''CREATE TABLE IF NOT EXISTS personLocation
                     (id integer PRIMARY KEY,
                      city text,
                      state text,
                      country text,
                      postcode text
                     )''')
        self.c.execute('''CREATE TABLE IF NOT EXISTS personLocationStreet
                     (
                      id integer PRIMARY KEY,
                      number text,
                      name text
                     )''')
        self.c.execute('''CREATE TABLE IF NOT EXISTS personLocationCoordinates
                     (
                      id integer PRIMARY KEY,
                      latitude text,
                      longitude text
                     )''')
        self.c.execute('''CREATE TABLE IF NOT EXISTS personLocationTimezone
                     (
                      id integer PRIMARY KEY,
                      offset text,
                      description text
                     )''')
        self.c.execute('''CREATE TABLE IF NOT EXISTS personLogin
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
        self.c.execute('''CREATE TABLE IF NOT EXISTS personDOB
                     (
                      id integer PRIMARY KEY,
                      date text,
                      age integer
                     )''')
        self.c.execute('''CREATE TABLE IF NOT EXISTS personRegistered
                     (
                      id integer PRIMARY KEY,
                      date text,
                      age integer
                     )''')
        self.c.execute('''CREATE TABLE IF NOT EXISTS personId
                     (
                      id integer PRIMARY KEY,
                      name text,
                      value text
                     )''')
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
