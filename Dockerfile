FROM python:3.10

COPY . .
WORKDIR .
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt