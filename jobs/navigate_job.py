
import time
from rpa.jobs.job import Job
from rpa.drivers.context import Context


class NavigateJob(Job):

    _url: str
    _time: int

    def __init__(self, url: str, time=2):
        self._url = url
        self._time = time

    def run_logic(self, context: Context):
        context.current_url = self._url
        context.driver.get(url=self._url)
        time.sleep(self._time)
