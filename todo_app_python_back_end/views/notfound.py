"""
This module contains the view for the 404 page.
"""

from pyramid.view import notfound_view_config


@notfound_view_config(renderer='todo_app_python_back_end:templates/404.jinja2')
def notfound_view(request):
    request.response.status = 404
    return {}
