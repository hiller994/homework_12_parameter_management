import os
import tests.demoqa

def path(file_name):
    return os.path.abspath(
        os.path.join(os.path.dirname(tests.demoqa.__file__), f'../test_file/{file_name}')
    )