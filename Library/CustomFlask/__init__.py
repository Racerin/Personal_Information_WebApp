import dataclasses
from flask.sessions import SessionInterface, SessionMixin

# Custom Sessions: https://www.programmersought.com/article/26613776483/


# @dataclasses.dataclass
class MySession(dict, SessionMixin):
    logged_in : bool = False
    username : str = ""

    def __init__(self, *_args, **kwargs):
        super().__init__(**kwargs)


class MySessionInterface(SessionInterface):
    session_class = MySession
