
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from rpa.jobs.job import Job
from rpa.drivers.context import Context


class NavigateJob(Job):

    _url: str

    def __init__(self, url: str):
        self._url = url

    def run_logic(self, context: Context):
        context.current_url = self._url
        context.driver.get(url=self._url)
        time.sleep(5)

        
