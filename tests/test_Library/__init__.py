import unittest
import Library
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
    def test_valid(self):
        pass


if __name__ == "__main__":
    unittest.main()