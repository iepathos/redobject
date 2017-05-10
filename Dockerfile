FROM python:3.6.0
MAINTAINER Glen Baker <iepathos@gmail.com>

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt

RUN python -m nltk.downloader punkt

RUN git clone https://github.com/iepathos/marlowe_dataset.git

ENTRYPOINT ["python"]
CMD ["server.py"]