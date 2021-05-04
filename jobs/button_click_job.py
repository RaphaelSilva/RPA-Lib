from typing import Callable
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from jobs import Job
from drivers import Context

Click: Callable[[WebElement], None] = lambda el: el.click()


class ButtonClickJob(Job):

    _path: str
    _method: str

    def __init__(self, path: str, method='find_element_by_xpath'):
        super().__init__()
        self._path = path
        self._method = method

    def run_logic(self, context: Context):
        try:
            context.element = getattr(context.driver, self._method)(self._path)
            Click(context.element)
        except NoSuchElementException:
            print(NoSuchElementException)
