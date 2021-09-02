FROM python:3.9.5-slim

LABEL Author="Aro RAZAFINDRAKOLA"

WORKDIR /project
ADD . /project

RUN pip install -r requirements.txt

##flask
EXPOSE 5000
CMD ["python", "index.py"]

##gunicorn
#EXPOSE 8080
#CMD ["gunicorn", "index:server"]
