FROM ubuntu:16.04
LABEL MAINTAINER Jieyi<pokkbaby@gmail.com>

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
ADD . /diamon-dam
WORKDIR /diamon-dam
RUN pip install -r requirements.txt
EXPOSE 8888
ENTRYPOINT ["python"]
CMD ["flask-docker.py"]