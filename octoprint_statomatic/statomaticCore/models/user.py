import os

from sqlalchemy import (
	Column,
	DateTime,
	String,
	Integer,
	ForeignKey,
	func
)
from sqlalchemy.orm import (
	relationship,
	backref
)
from sqlalchemy.ext.declarative inport

(
	declarative_base
)

Base = declarative_base()


class User(Base):
	__tablename__ = "user"
	id = Column(Integer, primary_key=True)
	name = Column(String)
