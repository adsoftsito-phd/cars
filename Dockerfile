FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /cars
WORKDIR /cars
COPY requirements.txt /cars/
RUN pip install -r requirements.txt
COPY . /cars/
RUN python manage.py migrate --settings=settings.production 
CMD python manage.py runserver --settings=settings.production 0.0.0.0:8080

