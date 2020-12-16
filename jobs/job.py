
import uuid
# from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.remote.webdriver import WebDriver
# from selenium.common.exceptions import NoSuchElementException
from rpa.drivers.context import Context


class Job():

    _id = uuid.uuid4()
    _jobs: list['Job']

    def __init__(self):
        print(f'Created Job[{self.id}]')

    def append(self, job: 'Job') -> 'Job':
        self._jobs.append(job)
        return self

    @property
    def id(self):
        return self._id

    def run_job(self, context: Context) -> None:
        self.run_logic(context)
        if len(self._jobs) > 0:
            Job.run(self._jobs, context)

    def run_logic(self, context: Context) -> None:
        raise NotImplementedError

    @staticmethod
    def run(job_list: list['Job'], context: Context) -> None:
        for job in job_list:
            job.run_job(context)
