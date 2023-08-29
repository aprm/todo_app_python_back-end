"""
Helper methods and classes for unit tests.
"""
from unittest.mock import Mock
from pyramid.testing import DummyRequest


class MockDbSession:
    """
    Mocks a SQLAlchemy database session.
    """
    def __init__(self):
        self.items = []

    def query(self, cls_):
        return Mock(all=lambda: self.items)
    
    def add(self, item):
        self.items.append(item)
    
    @staticmethod
    def flush():
        pass


def get_mock_request(post_params=None):
    """
    Returns a mocked Pyramid request object.
    """
    return DummyRequest(
        dbsession=MockDbSession(),
        post=post_params
    )
