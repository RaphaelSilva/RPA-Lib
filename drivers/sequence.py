from selenium.webdriver.remote.webdriver import WebDriver
from rpa.jobs.job import Job
from rpa.drivers.context import Context


class Sequence():
    _job_list: list[Job]
    _context: Context

    def __init__(self, seq: list[Job]):
        self._job_list = seq

    def execute(self, driver: WebDriver):
        self._context = Context(driver)
        Job.run(self._job_list, self._context)

    @property
    def context(self):
        return self._context
