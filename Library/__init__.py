import ast, enum, copy, types
from collections.abc import Collection
from dataclasses import dataclass, fields, Field, asdict
import PARAM


def value_type_of_str(str1, type1):
    """Returns value of type 'type1' given a string input."""
    #FOUND A BETTER FUNCTION, MultiDict
    if issubclass(type1, Collection):
        try:
            # obj = eval(str1)
            obj = ast.literal_eval(str1)
            if isinstance(obj, Collection):
                return obj
        except:
            return type1(str1)
    else:
        try:
            return type1(str1)
        except:
            return type1()


@dataclass
class Person():
    first_name : str = ""
    middle_name : str = ""
    maiden_name : str = ""
    last_name : str = ""
    birthday : str = ""
    gender : str = PARAM.GENDER.UNDEFINED
    description : str = "Hi!"
    title : str = PARAM.TITLE.NONE

    _gender = gender

    @property
    def gender(self): 
        return self._gender
        
    @gender.setter
    def gender(self, val):
        self._gender = PARAM.GENDER.assign(val)

    necessary_fields = ['first_name', 'last_name',]

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def _filter_from_dict(cls, nm, val):
        """Filter attribute from client to 'Person' object."""
        #Any necessary filtering place here.
        return val

    @staticmethod
    def _get_val_from_dict(dict1, name, type1) -> "types.Type[type]":
        """Get value from a multidict variable w.r.t class 'Person'."""
        try:
            val = dict1.get(name, type=type1)   #https://stackoverflow.com/a/12551565/6556801
            return val
        except TypeError:
            if isinstance(type1, PARAM.GENDER):
                return dict1[name]
                # return attr1

    @classmethod
    def from_dict(cls, multidict1) -> "Person":
        """Constructs an object from the arguments passed into 'request' at that moment and thread. """
        self = cls()
        #https://stackoverflow.com/a/51953411/6556801
        field_types = cls.field_types()
        for key, type1 in field_types.items():
            # val = cls._get_val_from_dict(multidict1, key, type1)
            val = multidict1.get(key, type1())
            val = cls._filter_from_dict(key, val)
            setattr(self, key, val)
        return self

    @classmethod
    def field_types(cls) -> dict:
        """Returns a dictionary of field_name:field_type attributes"""
        return {field.name:field.type for field in fields(cls)}

    def valid(self) -> bool:
        """Response on whether data supplied is sufficient for submitting to database/file."""
        are_populated = [bool(getattr(self, fld_nm)) for fld_nm in self.necessary_fields]
        return all(are_populated)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def success_rep(self)->str:
        str1 = f"Name: {self.name}"
        return str1

    def success_rep2(self)->str:
        """Return a nice looking __rep__ string for html."""
        strings = []
        json_dict = self.to_json()
        for fld in fields(self):
            # val = getattr(self, fld.name)
            val = json_dict.get(fld.name, None)
            if val:
                str1 = f"{fld.name.title().replace('_',' ')}: {val}"
                strings.append(str1)
        return ", ".join(strings)

    def to_json(self):
        """Converts 'Person' to json-ready dict"""
        dict1 = self.__dict__
        #Updating gender to type str
        gender = dict1.get("gender", PARAM.GENDER.UNDEFINED)
        gender = gender if gender else PARAM.GENDER.UNDEFINED   #deals with 'None'
        dict1.update({'gender':gender.value})
        return dict1


@dataclass
class User():
    username : str
    password : str

    def __post_init__(self):
        """Instantiation after dataclass implementation"""
        pass

    def salted_password(self) -> bytes:
        """Returns a salted password."""
        #NB. FOR NOW, USE THIS.
        return self.password.encode()

    def username_password(self):
        return self.username, self.password

    @classmethod
    def dumb_user(cls):
        self = cls(username="Foo", password="Password#1234")
        return self
