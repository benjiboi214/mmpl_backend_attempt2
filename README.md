# MMPL Backend
Description of what this project is here for.

## Environment
All possible ENV vars can be found at  `./.env.example`. 
Copy this file to .env by running the following command.

````bash
cp ./.env.example ./.env
````

Modify this file as required and run the app using the commands found in [Building](#building-locally)

If you have lost your Pipfile, you may need to restore one from the lock. Ensure the Pipfile is not in the base dir and run the following to extract.
````bash
./build_scripts/local/extract_pipfile.sh
````
You need jq installed on your machine to run this successfully.

## Building Locally
Building and testing locally is always encouraged before submitting a pull request, to ensure that tests pass and there are no issues with linting and style.

These commands assumes there is no other docker activity on the build server. 
For example, the run command assumes the most recently built image is the one you want to run.

Ensure the current environment is cleared on docker to get rid of dead containers, claenup dangling images and remove test reports.
````bash
./build_scripts/local/clean.sh
````

Build the django app image.
````bash
./build_scripts/local/build.sh
````

Run the app.
````bash
./build_scripts/local/run.sh
````

Print the logs to sdout
````bash
./build_scripts/local/logs.sh
````

Stop the app.
````bash
./build_scripts/local/stop.sh
````

## Building Remotely
Builds on this project are executed from AWS. Environment that deviates from the defaults is stored in the SSM and retrieved at runtime.

The `./build_scripts/remote/` directory contains the scripts used for remotely building, pushing and running tests when used in AWS.

The `./build_config/remote/` directory contains the config for each container used in the application.

## Testing
Test the images locally by running the following commands. You may need to specify where you are running the app in order for the functional tests to find the app and run its tests.

Unit test the apps.
````bash
./build_scripts/local/unit_test.sh
````

Test the app end to end with Selenium.
````bash
./build_scripts/local/func_test.sh
````


## DB 
There is functionality to retrieve the DB from AWS and copy it locally.
````bash
./build_scripts/local/get_db.sh
````

## Contributing
Haven't thought that far ahead. Open an issue on Github with any questions.
Run the pre commit script to validate your code before opening a pull request.
````bash
./build_scripts/local/pre_commit.sh
````

revert!?