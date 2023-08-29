from pyramid.view import view_config
from pyramid.response import Response
from sqlalchemy.exc import SQLAlchemyError

from .. import models


@view_config(route_name='home', renderer='todo_app_python_back_end:templates/home.jinja2')
def get_items(request):
    """
    View that returns a list of items from the database.
    """
    try:
        query = request.dbsession.query(models.TodoItem)
    except SQLAlchemyError:
        return Response("Internal Error", content_type='text/plain', status=500)
    return {
        'todolist': query.all()
    }


@view_config(route_name='add')
def add_item(request):
    """
    View that adds a new item to the database.
    """
    try:
        name = request.POST.get('name')
        if not name:
            return Response("Task name should not be empty!", content_type='text/plain', status=400)
        new_item = models.TodoItem()
        new_item.name = name
        request.dbsession.add(new_item)
        request.dbsession.flush()
    except SQLAlchemyError:
        return Response("Internal Error", content_type='text/plain', status=500)
    return Response("Task added", content_type='text/plain', status=301, location='/')


@view_config(route_name='delete')
def delete_item(request):
    """
    View that deletes an item from the database.
    """
    try:
        id = request.POST.get('id')
        if not id:
            return Response("Task id should not be empty!", content_type='text/plain', status=400)
        item = request.dbsession.query(models.TodoItem).filter_by(id=id).first()
        request.dbsession.delete(item)
        request.dbsession.flush()
    except SQLAlchemyError:
        return Response("Internal Error", content_type='text/plain', status=500)
    return Response("Task deleted", content_type='text/plain', status=301, location='/')


@view_config(route_name='complete')
def complete_item(request):
    """
    View that marks an item as completed in the database.
    """
    try:
        id = request.POST.get('id')
        if not id:
            return Response("Task id should not be empty!", content_type='text/plain', status=400)
        item = request.dbsession.query(models.TodoItem).filter_by(id=id).first()
        item.completed = True
        request.dbsession.flush()
    except SQLAlchemyError:
        return Response("Internal Error", content_type='text/plain', status=500)
    return Response("Task completed", content_type='text/plain', status=301, location='/')
