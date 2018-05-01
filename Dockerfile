FROM python:2.7

ADD requirements.txt requirements.txt
ADD app.py app.py
ADD settings.py settings.py
ADD templates templates

RUN pip install -r requirements.txt

ENV URL_CONFIG=coucou
ENV URL_VOTE=hello
ENV FLASK_APP=app.py

CMD flask run --host=0.0.0.0