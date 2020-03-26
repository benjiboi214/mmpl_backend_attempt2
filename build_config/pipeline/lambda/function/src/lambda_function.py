import base64
import os
import time
import urllib

import boto3
import pytest

client = boto3.client('codedeploy')

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


def send_sms(event, context):
    to_number = "+61429227281"
    from_number = "MMPL Staging Pipeline"
    body = "Pipeline has finished building. Ready to deploy."

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

    # encode the parameters for Python's urllib
    data = urllib.parse.urlencode(post_params).encode()
    req = urllib.request.Request(populated_url)

    # add authentication header to request based on Account SID + Auth Token
    authentication = "{}:{}".format(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    base64string = base64.b64encode(authentication.encode('utf-8'))
    req.add_header("Authorization", "Basic %s" % base64string.decode('ascii'))

    print("req:")
    print(req)
    
    try:
        # perform HTTP POST request
        with urllib.request.urlopen(req, data) as f:
            print("Twilio returned {}".format(str(f.read().decode('utf-8'))))
    except Exception as e:
        # something went wrong!
        return e

    return "SMS sent successfully!"
