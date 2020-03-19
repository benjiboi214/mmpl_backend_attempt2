import os
import pprint

import importlib_metadata

from selenium.webdriver.common.keys import Keys
import boto3


import pytest
from functional_tests import NewVisitorTest

client = boto3.client('codedeploy')


def lambda_handler(event, context, *args, **kwargs):
    # Get and print the environment for debugging.
    env_var = os.environ
    os.environ['PYTEST_LAMBDA_FLAG'] = "True"

    exit_code = pytest.main([
        "-s", # Disable capturing of syslog for debugging
        "-p", "no:cacheprovider", # Don't try to write pycache files
        "/var/task/src/functional_tests.py"
    ], plugins=[])

    if exit_code == pytest.ExitCode.OK:
        print("=== Test Condition PASSED ===")
        response = client.put_lifecycle_event_hook_execution_status(
            deploymentId=event['DeploymentId'],
            lifecycleEventHookExecutionId=event['LifecycleEventHookExecutionId'],
            status='Succeeded'
        )
        return
    else:
        print("=== Test Condition FAILED ===")
        response = client.put_lifecycle_event_hook_execution_status(
            deploymentId=event['DeploymentId'],
            lifecycleEventHookExecutionId=event['LifecycleEventHookExecutionId'],
            status='Failed'
        )
        return