FROM python:3.8-slim

COPY requirements.txt /app/requirements.txt
WORKDIR /app 

RUN apt-get update
RUN apt-get -y install gcc
RUN pip3 install -r requirements.txt

COPY app.py app.py
COPY images /app/images

CMD ["streamlit", "run", "app.py"]