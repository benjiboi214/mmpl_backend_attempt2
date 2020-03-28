import base64
import os
import time

import boto3
import pytest
import requests

client = boto3.client('codedeploy')
code_pipeline = boto3.client('codepipeline')

TWILIO_SMS_URL = "https://api.twilio.com/2010-04-01/Accounts/{}/Messages.json"
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")


def functional_tests(event, context, *args, **kwargs):
    time.sleep(20)

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


def put_job_success(job, message):
    """Notify CodePipeline of a successful job

    Args:
        job: The CodePipeline job ID
        message: A message to be logged relating to the job status

    Raises:
        Exception: Any exception thrown by .put_job_success_result()

    """
    print('Putting job success')
    print(message)
    code_pipeline.put_job_success_result(jobId=job)


def put_job_failure(job, message):
    """Notify CodePipeline of a failed job

    Args:
        job: The CodePipeline job ID
        message: A message to be logged relating to the job status

    Raises:
        Exception: Any exception thrown by .put_job_failure_result()

    """
    print('Putting job failure')
    print(message)
    code_pipeline.put_job_failure_result(jobId=job, failureDetails={'message': message, 'type': 'JobFailed'})


def send_sms(event, context):
    print("EVENT: ")
    print(event)
    print("CONTEXT")
    print(context)

    job_id = event['CodePipeline.job']['id']

    to_number = "+61429227281"
    from_number = "MMPL"
    body = "Ready to Deploy. https://github.com/benjiboi214/mmpl_backend/commit/%s" % \
        {event['CodePipeline.job']['data']['inputArtifacts'][0]['revision']}

    if not TWILIO_ACCOUNT_SID:
        return "Unable to access Twilio Account SID."
    elif not TWILIO_AUTH_TOKEN:
        return "Unable to access Twilio Auth Token."
    elif not to_number:
        return "The function needs a 'To' number in the format +12023351493"
    elif not from_number:
        return "The function needs a 'From' number in the format +19732644156"
    elif not body:
        return "The function needs a 'Body' message to send."

    # insert Twilio Account SID into the REST API URL
    populated_url = TWILIO_SMS_URL.format(TWILIO_ACCOUNT_SID)
    post_params = {"To": to_number, "From": from_number, "Body": body}

    # add authentication header to request based on Account SID + Auth Token
    authentication = "{}:{}".format(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    base64string = base64.b64encode(authentication.encode('utf-8'))

    headers = {
        'Authorization': "Basic %s" % base64string.decode('ascii')
    }

    response = requests.request("POST", populated_url, data=post_params, headers=headers)

    if 200 <= response.status_code <= 299:
        put_job_success(job_id, "SMS sent successfully! " + str(response.status_code))
        return
    else:
        put_job_failure(job_id, "Failed to send SMS")
