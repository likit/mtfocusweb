FROM python:3.7.2
ENV PYTHONUNBUFFERED 1
RUN mkdir /mtclan/
WORKDIR /mtclan
COPY mtclan/requirements.txt /mtclan/requirements.txt
RUN pip install -U pip && pip install -r requirements.txt
