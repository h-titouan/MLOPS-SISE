FROM python:3.8-slim

COPY requirements.txt /app/requirements.txt
COPY iris_ML_v1.joblib /app/iris_ML_v1.joblib

WORKDIR /app 

RUN apt-get update
RUN apt-get -y install gcc
RUN pip3 install -r requirements.txt

COPY app.py app.py


CMD ["uvicorn", "--host", "0.0.0.0", "app:app"]