FROM python:3.9.12

WORKDIR /music-hack

RUN apt-get -y update
RUN apt-get install -y ffmpeg=7:4.3.6-0+deb11u1
RUN apt-get install -y libsndfile1=1.0.31-2

COPY requirements.txt ./
RUN pip install --no-cache-dir Cython==0.29.28
RUN pip install --no-cache-dir numpy==1.21.6
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT /bin/bash

