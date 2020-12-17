

class User():
    _name: str
    _login: str
    _password: str

    def __init__(self, name: str, login: str, password: str):
        self._name = name
        self._password = password
        self._login = login

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def login(self) -> str:
        return self._login

    @login.setter
    def login(self, login: str):
        self._login = login

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, password: str):
        self._password = password
