
import uuid
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
# from selenium.common.exceptions import NoSuchElementException
from rpa.drivers.context import Context


class Job():
    _id = uuid.uuid4()

    def __init__(self):
        print(f'Created Job[{self.id}]')

    @property
    def id(self):
        return self._id

    def run_logic(self, context: Context) -> None:
        raise NotImplementedError
