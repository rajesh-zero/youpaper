FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /youpaper
ADD . /youpaper
COPY ./requirements.txt /youpaper/requirements.txt
RUN pip install -r requirements.txt
RUN 
COPY . /youpaper