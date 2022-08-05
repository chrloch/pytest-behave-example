import pytest
__doc__ = 'This file creates a context fixture for pytest that is required to call behave test steps'

class SimpleContext(dict):
     def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         self.__dict__ = self


@pytest.fixture(scope='session')
def context(request):
    'A simple context to allow pytest to use feature steps'
    if not hasattr(context, '_instance'):
        context._instance = SimpleContext()
    return context._instance
