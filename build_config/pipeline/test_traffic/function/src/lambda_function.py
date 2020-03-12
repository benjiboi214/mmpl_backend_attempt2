import os
import pprint

import importlib_metadata

from webdriver_wrapper import WebDriverWrapper
from selenium.webdriver.common.keys import Keys

import pytest
from functional_tests import NewVisitorTest

def lambda_handler(*args, **kwargs):
    driver = WebDriverWrapper().driver
  
    # Get the list of user's 
    # environment variables 
    env_var = os.environ 
    
    # Print the list of user's 
    # environment variables 
    print("User's Environment variable:") 
    pprint.pprint(dict(env_var), width = 1) 


    exit_code = pytest.main([
        "-p", "no:cacheprovider",
        "/var/task/src/functional_tests.py"
    ], plugins=[])
    print("EXIT CODE")
    print(exit_code)