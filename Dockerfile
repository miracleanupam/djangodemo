FROM python:3

RUN apt -y update

ENV PYTHONUNBUFFERED=1
ENV DJANGO_SUPERUSER_PASSWORD=nimda
ENV DJANGO_SUPERUSER_USERNAME=admin
ENV DJANGO_SUPERUSER_EMAIL=admin@admin.com

WORKDIR /app

# Generally a good way is to combine all the RUN commands into one so that
# If any command changes, the layer with the command is over-ridden
# But, let it be for this one
RUN git clone https://github.com/miracleanupam/djangodemo.git
RUN mv djangodemo/* .

RUN pip install -r requirements.txt

RUN chmod +x entrypoint.sh
#RUN ./entrypoint.sh

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]