import ast
from collections.abc import Collection
from dataclasses import dataclass, fields, Field


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


class Gender(str):pass


@dataclass
class Person():
    first_name : str = ""
    last_name : str = ""
    age : int = 0
    gender : str = ""

    necessary_fields = ['first_name', 'last_name',]

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def from_dict(cls, multidict1):
        """Constructs an object from the arguments passed into 'request' at the moment. Return the object."""
        self = cls()
        #https://stackoverflow.com/a/51953411/6556801
        field_types = cls.field_types()
        for nm,type1 in field_types.items():
            val = multidict1.get(nm, type1(), type=type1)
            setattr(self, nm, val)
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

    def success_rep(self):
        str1 = f"Name: {self.name}"
        return str1