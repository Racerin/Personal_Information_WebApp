import unittest, os, shutil, tempfile
import PARAM
from Library import Database
import app as App


app = App.testing.FlaskClient


class TestBasic(unittest.TestCase):

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
    # def login(self, **kwargs):
    #     return App.app.post("/login", data=kwargs, follow_redirects=True)
    # def logout(self):
    #     return App.app.get('/logout', follow_redirects=True)
    # def register(self, **kwargs):
    #     ans = App.app.post("/form", data=kwargs, follow_redirects=True)
    #     print("This is the answer of the register function: ", type(ans), dir(ans))
    #     return ans 
    
    @classmethod
    def setUpClass(cls):
        """Builtin method that runs once before all unit tests."""
        db_fd, db_path = tempfile.mkstemp()
        #Create Temporary database
        db_filename = "database.db"
        #Get name of new temporary database
        #
        if db_filename != cls.db_temp_filename and not os.path.exists(cls.db_temp_filename):
            #Create new database
            shutil.copy(db_filename, cls.db_temp_filename)
        #Start Database
        App.app.database = Database.SQLiteDatabase(filename=cls.db_temp_filename)

    def setUp(self):
        App.app.config['whatever_setting'] = True

    def test_valid_user_registration_and_login(self):
        """Register and Login User."""
        #Register
        response = self.register(**self.eg_user_register_dict)
        self.assertEqual(response.status_code, 200)
        print("This is response.data:", response.data)
        #Login
        login_dict = dict()
        response1 = self.login()
        self.assertEqual(response1.status_code, 200)

    @classmethod
    def tearDownClass(cls):
        #Close the database
        App.app.database.close()
        #Delete database file
        # shutil.rmtree
        os.remove(cls.db_temp_filename)


if __name__ == "__main__":
    unittest.main()