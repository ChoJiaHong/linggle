



FROM python:3.8


WORKDIR /

COPY ./requirements.txt /requirements.txt


RUN pip install --no-cache-dir --upgrade -r /requirements.txt

COPY ./geclec_project-db /geclec_project-db
EXPOSE 80
CMD ["uvicorn", "geclec_project-db.main:app", "--host", "0.0.0.0", "--port", "80"]

