import unittest, sys
import Library, PARAM
from Library import Person


class TestLibrary(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_value_type_of_str(self):
        args__returns = [
            ("", str, ""),
            ("mango", str, "mango"),
            ("10", int, 10),
            ("[1,3,5,7]",list, [1,3,5,7]),
            ('{"apple", "bat", "cat"}', set, {"apple", "bat", "cat"}),
            ("", int, 0),
        ]
        for *args, ret in args__returns:
            self.assertEqual(Library.value_type_of_str(*args), ret)
        #Error
        args__error = [
            (1, int, TypeError),
            # ("", 1, TypeError),
        ]
        for *args, err in args__error:
            self.assertRaises(err, Library.value_type_of_str(*args))


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.valid_person = Person(
            first_name="Darnell",
            middle_name="Regan Saleem",
            last_name="Baird",
            birthday="",
            gender=PARAM.GENDER.MALE,
            description="A legitimate Person."
            )
        self.female = Person(
            first_name="Desiree",
            middle_name="",
            last_name="",
            birthday="",
            gender=PARAM.GENDER.FEMALE,
            description="My mother."
        )
        # return super().setUp()

    def test_initialisation(self):
        #Throw Error for the following
        kwargs_error = [
            # ({}, TypeError),
            # ({"first_name":1}, TypeError)
        ]
        try:
            for kwargs, err in kwargs_error:
                with self.assertRaises(err):
                    Person(**kwargs)
        except AssertionError as err:
            print(kwargs, err)
            raise AssertionError(f"kwargs: '{kwargs}', Error: '{err}'.") from err

    def test_valid(self):
        pass

    def test_from_dict(self):
        valid_multidicts = [
            dict(first_name="Darnell", last_name="Baird"),
        ]
        valid_multidicts_ans = [
            Person(first_name="Darnell", last_name="Baird")
        ]
        for multidict, ans in zip(valid_multidicts, valid_multidicts_ans):
            psn = Person.from_dict(multidict)
            #UNITTEST IS ASSERTING BADLY. Might have to override 'Person's '__eq__' dunder method
            # self.assertEqual(psn, ans)


if __name__ == "__main__":
    unittest.main()