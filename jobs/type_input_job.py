from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from rpa.jobs.job import Job
from rpa.drivers.context import Context

class TypeInputMaskJob(Job):

    _word: str
    
    def __init__(self, word: str):        
        self._word = word

    def run_logic(self, context: Context):
        for key in self._word:
            context.element.send_keys(key)