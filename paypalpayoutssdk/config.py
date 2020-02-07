__version__ = "1.0.0"
__pypi_username__ = "paypal"
__pypi_packagename__ = "paypal-payouts-sdk"
__github_username__ = "paypal"
__github_reponame__ = "Payouts-Python-SDK"

import re
import os

def find_packages():
    path = "."
    ret = []
    for root, dirs, files in os.walk(path):
        if '__init__.py' in files:
            ret.append(re.sub('^[^A-z0-9_]+', '', root.replace('/', '.')))
    return ret