## BT Coding Challenge

### Structure of the application
- main.py file -> is the entrypoint to the application
- event.py -> this is the engine of the application where it calculates duration and session count
- events.txt -> is the file with log data for each user
- data_validation.py -> validates the input data from txt file such as timestamp, username and marker
- logger.py -> contains the rules for logging
- error_report.txt -> Lists all the errors caught from logging module
- tests -> folder that contains unit tests

### Running the application
1. Create a folder on your desktop/ documents. Pull the code from GitHub.
2. Set up virtual environment - Python version 3.10.1. ``` python -m venv venv```. 
The venv folder should be on the same level as src folder.
3. Set the PYTHONPATH in CLI ```export PYTHONPATH=~/bt_group_coding_challenge/src:$PYTHONPATH```
Activate the virtual env by typing ```source venv/bin/activate``` in CLI if using MacOS.
4. Enter the src folder in CLI ```cd src```
5. In CLI, type ```python main.py events.txt``` to run the application with log event data. 
There is no requirements.txt file to install additional libraries.
6. If you are in src folder, you can run unittest test as follows  ```python -m unittest tests/test_event.py```

### How the application works
1. The application checks for file ext. validation and whether the file exists
2. Then further validation checks are made regarding user log data from events.txt file. 
This is done by LogValidation.py file.
3. Depending on whether the marker is start or end it will either add the data to a 'queue' or 
calculate the duration in seconds respectively. The 'queue' system works using deque method in 
python collections module. It will append the data for 'start' marker and then popleft once both 
start and end session exists per user for each session/duration.
4. Username, session_count and duration are then printed by generate_report function in 
event.py file for each user.

Note:
- Char line is 89 (not 79).
- Functional/ Unit Testing needs to be finished. The following additional can be included:
  - FileNotFoundError
  - Checking for validation of timestamp, username and marker
  - Checking the whole application runs with the correct details
  - checking count of session and duration
