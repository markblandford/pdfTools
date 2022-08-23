# pdfTools

## Setup

I strongly recommend setting up a python [virtual environment](https://docs.python.org/3/tutorial/venv.html).

1. In  this directory run `python3 -m venv venv` to create the virtual environment.
2. Run `source venv/bin/activate` to activate the virtual environment.
3. You can verify you are using the virtual environment by running `which python` which will tell you which python program is in use. This should return a path within the virtual environment.
4. Install the dependencies / requirements `pip install -r requirements.txt`.
5. Once done, if you want to switch out of the virtual environment, simply run `deactive` to switch back to the OS default environment.

## Unit tests

[PyTest](https://docs.pytest.org) is the unit test framework in use.

To ensure there are no conflicts with the packages, a separate installation of the requirements for testing is required: `pip install -r ./tests/requirements.txt`

Run the tests using the command `python3 -m pytest` (we cannot simply run `pytest` as there is no `setup.py` in the project).

### Coverage

[Pytest-cov](https://pytest-cov.readthedocs.io/en/latest/index.html) is used for reporting coverage.

Run the unit tests with coverage, using the command `python3 -m coverage run -m pytest`

To then view the report, run `python3 -m coverage report`, or to generate a html report `python3 -m coverage html`. The report is saved to the [./htmlcov/](./htmlcov/) directory.

Note, remember you can combine the commands: `python3 -m coverage run -m pytest && coverage report`
