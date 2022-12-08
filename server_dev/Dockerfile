# /docker-server/server_dev/Dockerfile
FROM python:3.9.12

ENV PYTHONUNBUFFERED 1

RUN apt-get -y update
RUN apt-get -y install vim

RUN mkdir /srv/docker-server
ADD . /srv/docker-server

WORKDIR /srv/docker-server

#RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#RUN apt install libaio1
#RUN sh -c "echo /srv/docker-server/instantclient_21_8 > /etc/ld.so.conf.d/oracle-instantclient.conf"
#RUN ldconfig

#EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
