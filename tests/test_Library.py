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

    def test_initialisation(self):
        """
        'Person' class: 
        Ensure errors are thrown for invalid instantiation. 
        Ensure instantiation creates valid objects.
        """
        #Throw Error for the following
        kwargs_error = [
            ({}, TypeError),
            # ({"first_name":1}, TypeError)
        ]
        for kwargs, err in kwargs_error:
            msg = str((kwargs, err))
            with self.assertRaises(err, msg=msg):
                Person(**kwargs)

    def test_from_dict(self):
        """Test the method, 'from_dict'."""
        valid_multidicts = [
            dict(first_name="Darnell", last_name="Baird"),
        ]
        answers = [
            Person(first_name="Darnell", last_name="Baird")
        ]
        for multidict, ans in zip(valid_multidicts, answers):
            psn = Person.from_dict(multidict)
            #Error message
            dict_comp = {nm:getattr(ans,nm)==getattr(psn,nm) for nm in Person.field_names()}
            msg = str(dict_comp)
            self.assertEqual(psn, ans, msg=msg)


if __name__ == "__main__":
    unittest.main()