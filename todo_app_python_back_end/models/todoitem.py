from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Boolean
)

from .meta import Base


class TodoItem(Base):
    __tablename__ = 'todolist'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    completed = Column(Boolean, default=False)
