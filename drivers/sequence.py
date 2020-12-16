from selenium.webdriver.remote.webdriver import WebDriver
from rpa.jobs.job import Job
from rpa.drivers.context import Context


class Sequence():
    _job_list: list[Job]
    _context: Context

    def __init__(self, driver: WebDriver, seq: list[Job]):
        self._context = Context(driver)
        self._job_list = seq

    def execute(self):
        Job.run(self._job_list, self._context)
