import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

repo_name = '{{ cookiecutter.repo_name }}'
app_name = '{{ cookiecutter.app_name }}'

if not re.match(MODULE_REGEX, repo_name):
    print('ERROR: %s is not a valid name for a Django project!' % repo_name)
    # exits with status 1 to indicate failure
    sys.exit(1)

if not re.match(MODULE_REGEX, app_name):
    print('ERROR: %s is not a valid name for a Django app!' % app_name)
    # exits with status 1 to indicate failure
    sys.exit(1)