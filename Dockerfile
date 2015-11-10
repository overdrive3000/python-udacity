FROM python:3.5

ADD requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

RUN usermod -u 1000 user

USER user

CMD ["python", "code/app.py"]
