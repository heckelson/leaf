FROM python:3.11

RUN mkdir "/plant.mi"
WORKDIR "/plant.mi"

COPY ./*.py /plant.mi/
COPY Pipfile /plant.mi/
COPY Pipfile.lock /plant.mi/

COPY app/ /plant.mi/app/

RUN python -m venv .venv/
RUN python -m pip install pipenv

RUN python -m pipenv install

RUN python -m pipenv run python create_db_schema.py -y
RUN python -m pipenv run python fill_test_database.py

# pipenv run waitress-serve --port 5005 --url-scheme 'https' --call app:create_app
CMD ["python", "-m", "pipenv", "run", "waitress-serve", "--port", "5005", "--url-scheme", "'https'", "--call", "app:create_app"]

