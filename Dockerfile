FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY ./app/ /app/
COPY ./scripts/runserver.sh /scripts/runserver.sh
RUN python manage.py migrate
RUN python register_admin.py
EXPOSE 8000

ENTRYPOINT [ "bash", "/scripts/runserver.sh" ]