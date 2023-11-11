FROM alpine:3.14

COPY . /tmp/todo_app
RUN cd /tmp/todo_app && \
    # install dependencies
    apk add --no-cache python3 && \
    apk add --no-cache gettext && \
    wget https://bootstrap.pypa.io/get-pip.py && \
    python3 get-pip.py && \
    # copy config and local db files and install app
    cp production.ini /etc/production.ini && \
    cp todo_app_python_back_end.sqlite /var/todo_app_python_back_end.sqlite && \
    cp entrypoint.sh /entrypoint.sh && \
    pip3 install . && \
    # copy folder for alembic migrations
    mkdir /todo_app_python_back_end && \
    cp -r /tmp/todo_app/todo_app_python_back_end/alembic /todo_app_python_back_end/alembic && \
    # clean up
    rm -rf /tmp/todo_app

ENTRYPOINT ["sh", "/entrypoint.sh"]
