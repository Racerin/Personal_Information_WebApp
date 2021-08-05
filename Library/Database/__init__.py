from Library import Person, User
import os, json, time, sqlite3
from dataclasses import dataclass


def date_format(date, type1, type2) -> str:
    """Converts a string 'date' of type 'type1' to 'type2'."""
    final_date = date
    return date


@dataclass
class JsonDatabase():
    json_file_name : str = "json info.json"
    json_obj = dict()

    def __init__(self):
        """Load dict from json file"""
        self.load_json_file()

    #Context Manager Dunder Methods
    def __enter__(self):
        pass
    def __exit__(self, exc_type, exc_value, exc_tb):
        self.save_json_file()

    def recall(self, key, default=dict()):
        """Returns Json object if exists, else returns the type of the object"""
        try:
            return self.json_obj[key]
        except KeyError:
            return default

    def submit(self, key, val):
        self.json_obj[key] = val

    def load_json_file(self):
        """Assign json object of file to 'json_obj'. """
        if not os.path.exists(self.json_file_name):
            #Create file and object
            self.save_json_file()
        else:
            ##Retrieve the file
            with open(self.json_file_name) as file:
                self.json_obj = json.load(file)

    def save_json_file(self):
        with open(self.json_file_name, mode="w+") as file:
            json.dump(self.json_obj, file)


@dataclass
class SQLiteDatabase():
    filename : str = "::memory::"

    def __post_init__(self):
        #Open File
        self.conn = sqlite3.connect(self.filename)
        #Run database setup
        self.database_setup()

    def database_setup(self):
        """Create required properties and tables for the database if dont exist."""
        #Instantiate properties
        #Create table if not exist
        sqls = ["""CREATE TABLE IF NOT EXISTS 'USERS' (
            ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            USERNAME VARCHAR(50) NOT NULL,
            PASSWORD CHAR(20) NOT NULL
        );""",
        """CREATE TABLE IF NOT EXISTS 'PERSONALITIES' (
            ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            FNAME VARCHAR(20) NOT NULL, 
            MAIDENNAME VARCHAR(20),
            MNAME VARCHAR(20), 
            LNAME VARCHAR(20) NOT NULL,
            BIRTHDAY DATE,
            GENDER CHAR,
            USER_SUBMITTED_ID INTEGER
            );""",
        ]
        for sql in sqls:
            with self.conn as conn:
                conn.execute(sql)

    def create_user(self, user):
        """Adds user to database"""
        values = self.create_user_attributes(user)
        sql1 = """INSERT INTO USERS (USERNAME, PASSWORD) VALUES (?,?);"""
        with self.conn as conn:
            conn.execute(sql1, values)

    def valid_login(self, username, password):
        """Returns True if valid user credentials, else False"""
        return False

    def create_user_attributes(self, user):
        tup1 = (
            user.username,
            user.salted_password,
        )
        return tup1

    def _person_dict(self, person) -> dict:
        """Return the dictionary of 'person' needed to put in database."""
        #Create basic dictionary
        dict1 = vars(person)
        #Apply alterations
        dict1["birthday"] = person.birthday     #FOR NOW
        #Return dictionary
        return dict1

    def register_person(self, person):
        """Adds 'person' to database"""
        sql1 = """INSERT INTO PERSONALITIES (
            FNAME, MAIDENNAME, MNAME, LNAME, BIRTHDAY, GENDER, USER_SUBMITTED_ID
            ) VALUES (
                :first_name, :maiden_name, :middle_name, :last_name, :birthday, :gender, :description
            );"""
        with self.conn as conn:
            conn.execute(sql1, vars(person))

    def _row_to_person(self, row) -> Person:
        """Converts a 'row' object to a Person"""
        person = Person(
            first_name=row["FNAME"], 
            middle_name=row["MNAME"],
            maiden_name=row["MAIDENNAME"],
            last_name=row["LNAME"],
            birthday=date_format(row["BIRTHDAY"], 'sqlite', 'person'),
            description=row["DESCRIPTION"],
            )
        return person

    def get_persons(self) -> "list[Person]":
        """Returns a list of 'Person' objects from database."""
        #Get database information
        sql1 = "SELECT * FROM PERSONALITIES"
        with self.conn as conn:
            rows = conn.execute(sql1)
        #Get values of rows and put each values into person object.
        persons = []
        for r in rows:
            person = self._row_to_person(r)
            persons.append(person)
        return persons
