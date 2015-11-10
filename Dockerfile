FROM python:3.5

ADD requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

RUN echo "%sudo ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \ 
    useradd -u 5001 -G users,sudo -d /home/user --shell /bin/bash -m user && \
    echo "secret\nsecret" | passwd user && apt-get clean && \
    usermod -u 1000 user

USER user

CMD ["python", "code/app.py"]
