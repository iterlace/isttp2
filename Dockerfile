FROM python:3.10.4-buster

RUN mkdir /app
WORKDIR /app

COPY requirements/base.txt /tmp/requirements.txt
RUN python -m pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm -rf /root/.cache

COPY src/ /app/

CMD ["python", "/app/manage.py", "runserver", "0.0.0.0:8000"]