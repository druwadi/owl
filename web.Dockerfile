FROM python:3.9-buster

# Copy app files and download dependencies
RUN mkdir -p /usr/src/webservice/
COPY webservice/  /usr/src/webservice/
WORKDIR /usr/src/webservice
COPY requirements.txt ./
RUN pip install -r requirements.txt 

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]