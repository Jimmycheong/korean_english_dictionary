FROM ubuntu:latest
MAINTAINER Jimmy Cheong
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r app/requirements.txt
RUN pip install
ENTRYPOINT ["python"]
CMD ["app.py"]

RUN pwd
RUN ls