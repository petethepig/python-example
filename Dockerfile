FROM python:3.9

# RUN pip3 install pipenv
# COPY Pipfile ./Pipfile
# COPY Pipfile.lock ./Pipfile.lock
# RUN pipenv install

RUN pip3 install flask pyroscope-io

COPY main.py ./main.py

ENV FLASK_ENV=development
ENV PYTHONUNBUFFERED=1

CMD [ "python", "main.py" ]


