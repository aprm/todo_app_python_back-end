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
        return Mock(
            all=lambda: self.items,
            # todo: improve this to consider the filter_by parameters
            filter_by=Mock(
                return_value=Mock(
                    first=lambda: self.items[0]
                )
            )
        )

    def add(self, item):
        self.items.append(item)

    def delete(self, item):
        self.items.remove(item)

    @staticmethod
    def flush():
        pass


def get_mock_request(post_params=None):
    """
    Returns a mocked Pyramid request object with a mocked database session.
    """
    return DummyRequest(
        dbsession=MockDbSession(),
        post=post_params
    )
