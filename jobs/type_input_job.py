from typing import Callable
from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.remote.webdriver import WebDriver
# from selenium.common.exceptions import NoSuchElementException
from jobs import Job
from drivers import Context

Typing: Callable[[WebElement, str], None] = lambda el, text: [
    el.send_keys(key) for key in text]


class TypeInputMaskJob(Job):

    _word: str

    def __init__(self, word: str):
        super().__init__()
        self._word = word

    def run_logic(self, context: Context):
        Typing(context.element, self._word)
        # for key in self._word:
        #     context.element.send_keys(key)
