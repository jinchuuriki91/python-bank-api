FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /code
RUN pip install pipenv
COPY Pipfile Pipfile.lock /code/
RUN pipenv install --system --deploy --ignore-pipfile
COPY . /code/

CMD gunicorn -b 0.0.0.0:$PORT -c /code/guniconfig.py engine.wsgi:application
