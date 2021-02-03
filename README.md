# MBTA Deparature Time CLI Application

Given a route, direction, and stop, provides the next departure time.

#### Installation

Requires Python 3.x in order to run.

1. Initialize a virtualenv, if desired: `python -m venv <virtual-env-name>`
2. Activate virtualenv: `. <virtual-env-name>/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`

#### Running the application

Execute python from the root of the project on the cli entry point: `app.py`:

```bash
$ python app.py
```

#### Tests

This project uses `pytest` for testing.

From project root:

```
$ pytest
```

#### TODO

- Improve docstrings
- Add more tests
  - Achieve higher coverage
  - Test more non-happy path test cases
  - Test different MBTA API responseses
- Use a better cli library like PyInquirer
