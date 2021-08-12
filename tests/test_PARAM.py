from typing import Type
import unittest, string
import PARAM

class Test_ALL(unittest.TestCase):
    class ALL_SubclassIndifferent(PARAM.ALL):
        dog = 'dog'

    class ALL_Subclass1(PARAM.ALL):
        ALL = list(string.ascii_uppercase)

    class ALL_Subclass2(PARAM.ALL):
        ALL = list(string.ascii_lowercase)
        UNDEFINED = 'GOAT'


    def setUp(self):
        self.indiff = Test_ALL.ALL_SubclassIndifferent()
        self.obj1 = Test_ALL.ALL_Subclass1()
        self.obj2 = Test_ALL.ALL_Subclass2()

    def test_defaults(self):
        """
        Check for default values in subclass objects. 
        (Checking-out Abstract classes)
        """
        #What is 'ALL'
        self.assertEqual(self.indiff.ALL, [])
        self.assertEqual(self.obj1.ALL, list(string.ascii_uppercase) )
        self.assertEqual(self.obj2.ALL, list(string.ascii_lowercase))
        #What is 'UNDEFINED'
        self.assertEqual(self.indiff.UNDEFINED, None)
        self.assertEqual(self.obj1.UNDEFINED, None)
        self.assertEqual(self.obj2.UNDEFINED, 'GOAT')
        #Cannot instantiate abstract class

        #NB. WILL NOT BE AN ABSTRACT CLASS UNTIL AN ABSTRACT METHOD IS USED.
        # with self.assertRaises(TypeError):
        #     obj = PARAM.ALL()

    def test_verify(self):
        """Test verify method"""
        obj_val_ret = (
            #valid input
            # (self.indiff, 'grape', None),     #Will raise error
            (self.obj1, 'B', "B"),
            (self.obj2, 'l', 'l'),
            #'False' input
            (self.indiff, '', None),
            (self.obj1, '', None),
            (self.obj2, '', 'GOAT'),
        )
        for obj, val, ret in obj_val_ret:
            msg = f"Failed on: {obj}, {val}, {ret}"
            self.assertEqual(obj.verify(val), ret, msg=msg)
        obj_val_with_err = (
            (self.indiff, 'a'),
            (self.obj1, '123'),
            (self.obj2, '123'),
        )
        for obj, val in obj_val_with_err:
            msg = f"Failed on: {obj}, {val}."
            with self.assertRaises(ValueError, msg=msg):
                obj.verify(val)

    def test_assign(self):
        """Test assign method"""
        obj_val_ret = (
            #incorrect value
            (self.indiff, 'dog', None),
            (self.obj1, 'dog', 'A'),
            (self.obj2, 'dog', 'GOAT'),
            (self.obj2, 1, 'GOAT'),
            #correct values
            (self.obj1, 'G', 'G'),
            (self.obj2, 'g', 'g'),
        )
        for obj, val, ret in obj_val_ret:
            msg = f"Failed on: {obj}, {val}, {ret}."
            self.assertEqual(obj.assign(val), ret, msg=msg)