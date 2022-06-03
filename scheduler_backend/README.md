# Flask setup

## Install flask in virtual environment

```bash
sudo apt-get install python3-dev python3-pip python3-venv
```

From the scheduler_backend directory, run:

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install flask flask_sqlalchemy
```

## Run flask app

From the scheduler_backend directory, run:

```bash
. .venv/bin/activate
export FLASK_APP=backend
```

If you haven't initialized the database before, or want to clear the database:

```bash
flask initdb
```

Run the flask app:

```bash
flask run
```
