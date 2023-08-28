todo_app_python_back-end
========================

A simple todo app back-end written in Python using Pyramid and SQLAlchemy.

Requirements
------------
- Python 3.8+


Local develpment
----------
1. Clone the repository
2. Create a virtual environment
3. cd into the project directory
4. Run `pip install -e .` to install the project in editable mode.
5. Run `pip install -e ."[testing]"` to install testing requirements.
6. [Optional] Create / upgrade the database with `alembic -c development.ini upgrade head`
7. Run `pserve development.ini --reload` to start the local development server.

Local database upgrade
----------------------
1. Upgrade the database with `alembic -c development.ini upgrade head`

Running tests
-------------
1. TDB

Running the application in production
-------------------------------------
For simplicity, it is assumed that application will run the same way in production as in development, with the `pserve` command, without building / installing an egg and runnning application behind a separate WSGI server.

1. Clone the repository.
2. Set the database string in `production.ini`.
3. TBA