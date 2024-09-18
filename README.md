# Django Project template


## Installation

* Clone repository
```shell
# ssh
git clone git@github.com:Astro-edu-python/simple_kun_uz_parser_api.git

# or https
git clone https://github.com/Astro-edu-python/simple_kun_uz_parser_api.git
```

* Rename project name(and description[OPTIONAL]) in `pyproject.toml` to actual project name

* Install dependencies & activate environment
```shell
poetry install
poetry shell
```

## Install environment vars
* rename `example.env` to `.env` and set all values to actual values

## Run
Run project with make
```shell
make run

# RUN IT MANUALLY WITH SETTINGS
# dev
python manage.py runserver --settings=core.settings.dev

# with prod settings manually
python manage.py runserver --settings=core.settings.prod
# or with gunicorn
gunicorn core.wsgi:application -c server/gunicorn.conf.py
```
## !!!WARNING!!!
Don't use make run on production(use gunicorn/uvicorn etc.)

## NOTE
when you create your django apps in need directory, don't  forget register app in `INSTALLED_APPS` 
with absolute package path(aka `apps.your_app_path.apps.YourAppConfig`) and change `name` attribute 
on your app's `apps.py` to `apps.path_to_app`

## Server config
`server` dir contains server settings for the project

### gunicorn.conf.py
It's config file for gunicorn, it will be used in `site.supervisor.conf`

### site.supervisor.conf
* set `process_name` to some name
* set at command `/path/to/poetry/bin` to actual path to `poetry` and `/path/to/gunicorn.config.py` 
  to actual full path for `server/gunicorn.conf.py`
* set `directory` to full path to project directory
* set `user` to actual username which running these processes
* `stdout_logfile` is for all logs incoming to wsgi server, create some log file and set full path 

### CELERY
* Run worker with command `celery -A core worker -l INFO`
* Run beat with command `celery -A core beat -l INFO`
