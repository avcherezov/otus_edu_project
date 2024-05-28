import functools
from abc import ABC, abstractmethod

import allure

from errors import ERRORS


class ICommand(ABC):
    @abstractmethod
    def execute(self, command):
        pass


class Command:
    def __init__(self):
        self.store = []

    def add_command(self, command):
        self.store.append(command)

    def run_command(self):
        return self.store.pop(0).execute()

    def clear(self):
        self.store.clear()


class IOCContainer:
    def __init__(self):
        self._registrations = {}

    def register(self, key, implementation):
        self._registrations[key] = implementation

    def resolve(self, key):
        implementation = self._registrations.get(key)
        if not implementation:
            raise ValueError(f"No registration found for key: {key}")
        return implementation()


class ExceptionHandler:
    errors = ERRORS

    @classmethod
    def handle(clt, e, c):
        command = c.__class__.__name__
        exception = e.__class__.__name__

        raise Exception(clt.errors[command][exception])


def func_info(func):
    doc_str = func.__doc__
    allure_msg = None

    if doc_str:
        allure_msg = doc_str

    if not allure_msg:
        allure_msg = f"Вызываю функцию '{func.__name__}'"

    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        with allure.step(allure_msg):
            output = func(*args, **kwargs)
            if output:
                if isinstance(output, tuple):
                    with allure.step(output[0]):
                        return output
                else:
                    with allure.step(str(output)):
                        return output
    return _wrapper
