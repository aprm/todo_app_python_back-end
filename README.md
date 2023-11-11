todo_app_python_back-end
========================

A simple todo app back-end written in Python using Pyramid and SQLAlchemy.

Requirements
------------
- Python 3.8+
- [Install Pip](https://pip.pypa.io/en/stable/installation/#installation) (if not available), or upgrade to the latest version with `pip install --upgrade pip`


Local develpment
----------
1. Clone the repository.
2. Create a virtual environment.
3. `cd` into the project directory.
4. Run `pip install -e .` to install the project in editable mode.
5. Run `pip install -e ."[testing]"` to install testing requirements.
6. [If not done yet] Create / upgrade the database with `alembic -c development.ini upgrade head`
7. Run `pserve development.ini --reload` to start the local development server.

Local database upgrade (if needed)
----------------------
1. Upgrade the database with `alembic -c development.ini upgrade head`

Running tests
-------------
1. Run `pytest` from the project directory.

Running the application in production
-------------------------------------
For simplicity, it is assumed that application will run the same way in production as in development, with the `pserve` command, without building / installing an egg and runnning application behind a separate WSGI server.
(This is not recommended for production, but it is good enough for a simple demo.)

1. Clone the repository.
2. `cd` into the project directory.
3. Replace `$DB_CONNECTION_STRING` with the database connection string in `production.ini` file.
4. Run `pip install .` to install the project.
5. Run `pserve production.ini` to start the application.
6. The application will be available at http://localhost:6543. 

Production database upgrade (if needed)
---------------------------
1. Replace `$DB_CONNECTION_STRING` with the database connection string in `production.ini` file, and run `alembic -c production.ini upgrade head` from the project directory

Running the application in Docker
---------------------------------
1. Clone the repository.
2. `cd` into the project directory.
3. Run `docker build .` to build the Docker image.
4. Run `docker run -e DB_CONNECTION_STRING=<db_connection_string>  -p 6543:6543 <image_id>` to start the application.
   1. Replace `<db_connection_string>` with the database connection string, or use `sqlite:///var/todo_app_python_back_end.sqlite` to use the default local SQLite database.
   2. Replace `<image_id>` with the image ID from the previous step.

To upgrade the database (if needed), do one of the following:
* run `docker exec <container_id> alembic -c /etc/production.ini upgrade head`, where `<container_id>` is the ID of the running container - to run the upgrade from inside the container.
* replace `$DB_CONNECTION_STRING` with the database connection string in `production.ini` file, and run `alembic -c production.ini upgrade head` from the project directory
