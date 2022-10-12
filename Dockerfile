FROM python:3 
ENV PYTHONUNBUFFERED 1 
RUN apt-get -y update
RUN apt-get -y install vim 

RUN mkdir /srv/docker-server 
ADD . /srv/docker-server 

WORKDIR /srv/docker-server # 작업 디렉토리 설정

RUN pip install --upgrade pip 
RUN pip freeze > requirements.txt
RUN pip install -r requirements.txt 

EXPOSE 8000 
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"] 
