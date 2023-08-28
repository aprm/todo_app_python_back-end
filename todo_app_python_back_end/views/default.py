from pyramid.view import view_config
from pyramid.response import Response
from sqlalchemy.exc import SQLAlchemyError

from .. import models


@view_config(route_name='home', renderer='todo_app_python_back_end:templates/home.jinja2')
def get_items(request):
    try:
        query = request.dbsession.query(models.TodoItem)
    except SQLAlchemyError:
        return Response("Internal Error", content_type='text/plain', status=500)
    return {
        'todolist': query.all()
    }


@view_config(route_name='add', renderer='todo_app_python_back_end:templates/home.jinja2')
def add_item(request):
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
    return {
        'todolist': request.dbsession.query(models.TodoItem).all()
    }



