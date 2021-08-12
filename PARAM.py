import enum, abc


class ALL(abc.ABC):
# class ALL(metaclass=abc.ABCMeta):
    """Contains abstract methods to construct and work with an 'ALL' attribute for each subclass."""
    ALL = []
    UNDEFINED = None

    # @abc.abstractmethod
    @classmethod
    def verify(cls, val):
        """
        Verifies that val is a member of class' enumeration. 
        Also, converts false value into 1st 'ALL' element by default.
        """
        if val in cls.ALL:
            return val
        if not val: 
            return cls.UNDEFINED
        raise ValueError(f"Input '{val}' is not a viable {type(cls)} value.")

    # @abc.abstractmethod
    @classmethod
    def assign(cls, val):
        """Ensures that a proper element is returned."""
        if val in cls.ALL:
            return val
        #Else, return default
        if cls.UNDEFINED is not None:
            return cls.UNDEFINED
        elif cls.ALL:
            return cls.ALL[0]
        else:
            return cls.UNDEFINED


class HTML:
    HOME = "index.html"
    ABOUT = "about.html"
    CONTACT = "contact.html"
    FORM = "form.html"
    SUBMIT_SUCCESS = "success.html"
    SUBMIT_FAILURE = "failure.html"
    LOGIN = "login.html"
    SIGNUP = "signup.html"
    ERROR404 = "404.html"
    ERROR500 = "500.html"

class JSON:
    PERSONS = "persons"
    SESSIONS = "sessions"


# class GENDER(enum.Enum):
class GENDER(ALL):
    NA = "unavailable"
    UNDEFINED = "undefined"
    NONE = "none"
    MALE = "male"
    FEMALE = "female"
    ALL = [UNDEFINED, NA, NONE, MALE, FEMALE]
    FORM = [NA, MALE, FEMALE]

    # @classmethod
    # def verify(cls, str1) -> str:
    #     """Verifies that str1 is a string of 'GENDER'. Also, converts empty string into 'UNDEFINED'."""
    #     if not bool(str1): 
    #         return cls.UNDEFINED
    #     if str1 in cls.ALL:
    #         return str1
    #     raise ValueError(f"Input '{str1}' is not a viable GENDER value.")

    # @classmethod
    # def assign(cls, str1) -> str:
    #     """Ensures that a proper gender is returned."""
    #     if str1 in cls.ALL:
    #         return str1
    #     return cls.UNDEFINED

    # @classmethod
    # def __call__(cls):
    #     return cls.UNDEFINED


class TITLE:
    NONE = ""
    MR = "Mr."
    MRS = "Mrs."
    DOCTOR = "Dr."
    PROFESSOR = "Prof"


class DATABASE:
    FILENAME = 'database.db'