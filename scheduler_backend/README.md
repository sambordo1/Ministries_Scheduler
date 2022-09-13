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
python -m pip install flask flask_sqlalchemy flask_sock
```

## Relocate Qt resources into scheduler_backend directories

After building the Qt scheduler_frontend project for webassembly, we need to copy resources from the build directory into the backend directory.  This is currently automated as a build step in Qt (using the script [copy_wasm.sh](../copy_wasm.sh))

## Run flask app

From the scheduler_backend directory, run the script [run_flask.sh](../run_flask.sh) as ```./run_flask.sh``` or ```./run_flask.sh initdb``` to also initialize the database before running the flask app:
