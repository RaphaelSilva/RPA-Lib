# flake8: noqa
from .task import Task
from .clear import Clear

from pathlib import Path
if __name__ == '__main__':
    print('Running')
else:
    print('Importing', Path(__file__).resolve())
