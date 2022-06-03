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

## Relocate Qt resources into scheduler_backend directories

After building the Qt scheduler_frontend project for webassembly, need to copy resources from the build directory into the backend directory.  Run the following commands from the Ministries_Scheduler project root (TODO: automate this as build step in Qt):

```bash
mkdir scheduler_backend/templates
mkdir scheduler_backend/static
cp build-scheduler_frontend-WebAssembly*/appscheduler_frontend.html scheduler_backend/templates
cp build-scheduler_frontend-WebAssembly*/appscheduler_frontend.{js,wasm} scheduler_backend/static
cp build-scheduler_frontend-WebAssembly*/qtloader.js scheduler_backend/static
cp build-scheduler_frontend-WebAssembly*/qtlogo.svg scheduler_backend/static
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
