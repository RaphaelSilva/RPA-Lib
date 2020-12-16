from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver

class Context():

    _drive: WebDriver
    _element: WebElement
    _current_url: str
    
    def __init__(self, drive: WebDriver):
        self._drive = drive

    @property
    def driver(self) -> WebDriver:
        return self._drive

    @property
    def element(self) -> WebElement:
        return self._element
    
    @element.setter
    def element(self, el: WebElement):
        self._element = el

    @property
    def current_url(self):
        return self._current_url
    
    @current_url.setter
    def current_url(self, url):
        self._current_url = url