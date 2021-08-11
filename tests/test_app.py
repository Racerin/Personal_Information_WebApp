import unittest, os, shutil, tempfile, time
import PARAM
from Library import Database
from Library import Person, User
import app as App


app = App.app


class TestBasic(unittest.TestCase):

    db_filename = "database.db"

    eg_person_reg_dict = dict(
        first_name="Darnell",
        middle_name="Regan Saleem",
        maiden_name="",
        last_name="Baird",
        birthday="",
        gender=PARAM.GENDER.MALE,
        description="",
    )
    eg_user_login_dict = dict(
        username="user1",
        password="password!12345",
    )
    eg_user_register_dict = dict(
        username="doggy",
        email="sample@example.com",
        password1="password@12345",
        password2="password@12345",
    )

    #HELPER METHODS
    def login(self, client, username, password):
        dict1 = dict(username=username, password=password)
        return client.post('/login', data=dict1, follow_redirects=True)
    def logout(self, client):
        return client.post('/logout', follow_redirects=True)
    def register(self, client, **kwargs):
        ans = client.post("/form", data=kwargs, follow_redirects=True)
        return ans 
        
    # @pytest.fixture
    def client(self):
        return App.app.test_client()
    
    @classmethod
    def setUpClass(cls):
        """Builtin method that runs once before all unit tests."""
        #Create new database file with temp name
        cls.db_temp_file, cls.db_temp_filename = tempfile.mkstemp(suffix='.db')
        shutil.copy(cls.db_filename, cls.db_temp_filename)
        #Start Temp Database
        App.app.database = Database.SQLiteDatabase(filename=cls.db_temp_filename)

    def test_login_logout(self):
        """Ensures that log-in and log-out works."""
        #Create client
        client = self.client()
        username, password = User.dumb_user().username_password()
        #Login
        rv = self.login(client, username, password)
        self.assertIn(b"I love you.", rv.data)
        #Logout
        rv = self.logout(client)
        self.assertIn(b"hit", rv.data)
        #Login invalid username
        rv = self.login(client, username + "foo", password)
        #Login invalid user password
        rv = self.login(client, username, password + "foo")

    def test_create_personality(self):
        """Verify the types of forms created"""
        #Create client
        with self.client() as client:
            pass

    def t1est_valid_user_registration_and_login(self):
        """Register and Login User."""
        #Register
        response = self.register(**self.eg_user_register_dict)
        self.assertEqual(response.status_code, 200)
        #Login
        login_dict = dict()
        response1 = self.login()
        self.assertEqual(response1.status_code, 200)

    @classmethod
    def tearDownClass(cls):
        #Close the database
        App.app.database.close()


if __name__ == "__main__":
    unittest.main()