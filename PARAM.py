import enum


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
class GENDER:
    NA = "unavailable"
    UNDEFINED = "undefined"
    NONE = "None"
    MALE = "male"
    FEMALE = "female"
    ALL = [NA, UNDEFINED, NONE, MALE, FEMALE]

    @classmethod
    def verify(cls, str1) -> str:
        """Verifies that str1 is a string of 'GENDER'. Also, converts empty string into 'UNDEFINED'."""
        if not bool(str1): 
            return cls.UNDEFINED
        if str1 in cls.ALL:
            return str1
        raise ValueError(f"Input '{str1}' is not a viable GENDER value.")

class DATABASE:
    FILENAME = 'database.db'