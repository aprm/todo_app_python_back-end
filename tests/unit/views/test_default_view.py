from unittest.mock import Mock, patch
from sqlalchemy.exc import SQLAlchemyError

from todo_app_python_back_end.views.default import get_items, add_item
from tests.utils.helpers import get_mock_request, MockDbSession


def test_add_item():
    """
    Test that the add_item view adds a new item to the database.
    """
    request = get_mock_request(post_params={'name': 'test item'})
    response = add_item(request)

    assert response['todolist'][0].name == 'test item'


def test_add_item_without_name():
    """
    Test that the add_item view returns a 400 response when the name is empty.
    """
    request = get_mock_request(post_params={'name': ''})
    response = add_item(request)

    assert response.status_code == 400
    assert response.text == 'Task name should not be empty!'


def test_get_items_with_db_error():
    with patch.object(MockDbSession, 'query', side_effect=SQLAlchemyError):
        request = get_mock_request()
        response = get_items(request)
        assert response.status_code == 500
        assert response.text == 'Internal Error'
