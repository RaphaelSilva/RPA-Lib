from typing import Callable
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from rpa.jobs import Job, SubJob
from rpa.drivers import Context
from rpa.jobs.button_click_job import Click
from rpa.entitys import Stock


class SelectElementJob(Job):

    _path: str
    _method: str

    def __init__(self, path: str, method='find_element_by_xpath'):
        super().__init__()
        self._path = path
        self._method = method

    def run_logic(self, context: Context):
        try:
            el = getattr(context.driver, self._method)(self._path)
            context.element = el
        except NoSuchElementException:
            print(NoSuchElementException)


class ListJob(SelectElementJob):
    def __init__(self, path: str, method='find_elements_by_xpath'):
        super().__init__(path, method)


class SwitchFrameSelectJob(Job):

    _frame: str
    _path: str
    _method: str

    def __init__(self, frame: str, path: str, method='find_element_by_xpath'):
        super().__init__()
        self._frame = frame
        self._path = path
        self._method = method

    def run_logic(self, context: Context):
        try:
            context.driver.switch_to_frame(self._frame)
            el = getattr(context.driver, self._method)(self._path)
            context.element = el
        except NoSuchElementException:
            print(NoSuchElementException)


class LookupBy(SubJob):

    _compare_value: str
    _func: Callable[[WebElement], None]

    def __init__(self, value: str, func: Callable[[WebElement], None] = Click):
        self._compare_value = value
        self._func = func

    def exec(self, context: Context):
        li_list: list[WebElement] = context.element.find_elements_by_tag_name(
            'li')
        for li in li_list:
            html_input = li.find_element_by_tag_name('input')
            if html_input.get_attribute('value') == self._compare_value:
                if self._func is not None:
                    self._func(li)
                return


class LookupStock(SubJob):

    _value: str
    _func: Callable[[WebElement], None]

    def __init__(self, value: str, func: Callable[[WebElement], None] = Click):
        self._value = value
        self._func = func

    def exec(self, context: Context):        
        for el in context.element:
            Stock.facotry(el)