# plant.mi

A prototype for a citizen participation application
created over the course of a [hackathon at University of Vienna](http://web.archive.org/web/20230922082859/https://forschung.univie.ac.at/services/veranstaltungen-trainings/sonstige-veranstaltungen/hackathon/).

# Big Project cleanup

Aims to de-hackathon-ize the project by using proper tech. This is to have a presentable
prototype.

We're gonna try to follow this tutorial: https://marketsplash.com/how-to-integrate-flask-with-vue-js/

## Task list:

- [x] create vue project
- [x] rebuild navbar
- [x] integrate leaflet for the map
- [ ] figure out login/logout
- [ ] rebuild markers, popups, etc.
- [ ] rebuild fake dono, voting, etc.

---

## Run instructions

### Create a Python venv

```shell
$ python -m venv .venv/
```

### Activate the venv

Depends on the OS. Please check the python documentation: https://docs.python.org/3/library/venv.html

### Install stuff

```shell
(venv) $ pip install pipenv
(venv) $ pipenv install
```

should install all the stuff you need.

### Run

```shell
$ flask run
```

Should be enough to run the project from the app/ module.

## Contributing

Please use the provided pre-commit-hooks.

This can be done by installing pre-commit with pip or in the pipenv:

```shell
$ pipenv install pre-commit
```

Then installing it into the git hooks:

```shell
$ pre-commit install
```

On each commit, the hooks are run and reformat/clean up/... your code for consistency.
