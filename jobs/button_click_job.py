from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from rpa.jobs.job import Job
from rpa.drivers.context import Context


class ButtonClickJob(Job):

    _path: str
    _method: str

    def __init__(self, path: str, method = 'find_element_by_xpath'):
        self._path = path
        self._method = method

    def run_logic(self, context: Context):
        el = getattr(context.driver, self._method)(self._path)
        context.element = el
        context.element.click()
