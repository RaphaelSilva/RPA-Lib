from uuid import UUID, uuid4
# from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.remote.webdriver import WebDriver
# from selenium.common.exceptions import NoSuchElementException
from rpa.drivers import Context


class SubJob():

    def exec(self, context: Context):
        raise NotImplementedError


class Job():

    _id: UUID
    _sub_jobs: list[SubJob]

    def __init__(self):
        self._id = uuid4()
        self._sub_jobs: list[SubJob] = []

    def apply(self, sub_job: SubJob) -> SubJob:
        self._sub_jobs.append(sub_job)
        return self

    @property
    def id(self):
        return self._id

    def run_job(self, context: Context) -> None:
        self.run_logic(context)
        for sub_job in self._sub_jobs:
            sub_job.exec(context)

    def run_logic(self, context: Context) -> None:
        raise NotImplementedError

    @staticmethod
    def run(job_list: list['Job'], context: Context) -> None:
        for job in job_list:
            job.run_job(context)
