Answers to Assignar Python/Django Tech Test
===========================================

This repository contains answers to Assignar's technical test for the Junior Level Dev / Mid QA role.

The following tasks are covered in this repo:

1. Implement these user stories:
  - As a user, I should be able to upload an image with multiple labels.
  - As a user, I should be able to list all uploaded images with their correct labels.

2. Fix this bug:
  - As a user, I should be able to indicate labels for an image without needing to provide the confidence.

3. Create at least one UI test and one API test.

Comments have been provided inside `models.py` and `admin.py` to highlight the answers for tasks 1 and 2.


Setup
-----

### Installation

1. Please make sure that Python is installed in your machine and the version is at least 3.6. f-strings are used in the code and will not work on older versions of Python. Download Python [here](https://www.python.org/downloads/).

2. Create a virtual environment for this project (using `venv`, `virtualenv`) and activate it by running

		source virtualenv_name/bin/activate	

3. Install requisites by running

		pip  install -r requirements.txt

4. The selenium tests are also housed in this repository.  At a minimum, `chromedriver` should be installed for the tests to run using the default browser which is Chrome.
  * Download `chromedriver` from [here]([https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)).
  * Run `sudo apt-get install unzip` if unzip isn't installed yet, then unzip `chromedriver` at the desired location, e.g. `unzip ~/Downloads/chromedriver_linux64.zip -d /usr/bin`. 
  * Add the location to `PATH` if not there yet.

5. Install `geckodriver` if you wish to run the Selenium tests using Firefox.
  * Download `geckodriver` from [here]([https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases)).
  * Extract the file by running `tar -xvzf geckodriver*`.
  * Make it executable `chmod +x geckodriver`.
  * Add the driver to the `PATH` .

### Database setup

Setup the database and run migrations.

    $ ./manage.py migrate

Create your first superuser.

    $ ./manage.py createsuperuser
    
Load initial seed data.

    $ ./manage.py loaddata images

Development
----------------

### Running the server

    $ ./manage.py runserver

### Running the selenium tests

Create environment variables for the Django admin username and password. 

	$ export USERNAME=yourusername
	$ export PASSWORD=yourpassword

If you want to run the tests using headless Chrome, create this environment variable first.

	$ export HEADLESS=True

If you prefer to use Firefox, do

	$ export BROWSER=firefox

Run the tests using `pytest`.

	$ pytest selenium_tests/test_scripts/ -sv
