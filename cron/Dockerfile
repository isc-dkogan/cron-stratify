FROM python:3.10-slim

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

WORKDIR /user/src/app
COPY cron_module ./cron_module

CMD python3 -u cron_module