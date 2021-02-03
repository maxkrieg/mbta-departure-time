# MBTA Deparature Time

Given a route, direction, and stop, provides the next departure time.

#### Installation

Requires Python 3.x in order to run.

1. Initialize a virtualenv, if desired: `python -m venv <virtual-env-name>`

   - Activate virtualenv: `. <virtual-env-name>/bin/activate`

2. Install dependencies: `pip install -r requirements.txt`

#### Running the application

Execute python on the main entry point of the cli application, `app.py`.

```bash
$ python app.py
```

#### Tests

This project uses `pytest` for testing.

From project root:

```
$ pytest
```

##### TODO

- Add docstrings
- Add Pyhints
- Add more non-happy path test cases
