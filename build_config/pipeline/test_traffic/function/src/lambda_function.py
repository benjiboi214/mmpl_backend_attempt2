import os
import time

import boto3
import pytest

client = boto3.client('codedeploy')


def lambda_handler(event, context, *args, **kwargs):
    time.sleep(25)

    # Get and print the environment for debugging.
    os.environ['PYTEST_LAMBDA_FLAG'] = "True"

    exit_code = pytest.main([
        "-s",  # Disable capturing of syslog for debugging
        "-p", "no:cacheprovider",  # Don't try to write pycache files
        "-p", "no:warnings",
        "/var/task/src/functional_tests.py"
    ], plugins=[])

    if exit_code == pytest.ExitCode.OK:
        print("=== Test Condition PASSED ===")
        client.put_lifecycle_event_hook_execution_status(
            deploymentId=event['DeploymentId'],
            lifecycleEventHookExecutionId=event['LifecycleEventHookExecutionId'],
            status='Succeeded'
        )
        return
    else:
        print("=== Test Condition FAILED ===")
        client.put_lifecycle_event_hook_execution_status(
            deploymentId=event['DeploymentId'],
            lifecycleEventHookExecutionId=event['LifecycleEventHookExecutionId'],
            status='Failed'
        )
        return
