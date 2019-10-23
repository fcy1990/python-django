from django.test import TestCase

list = [('1', '美学班'), ('2', '武术班')]

for row in list:
    print(row)

import os
HERE = os.path.dirname(os.path.abspath(__file__))
print(HERE)


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)