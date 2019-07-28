
from sqlalchemy import (
	Column,
	DateTime,
	String,
	Integer,
	ForeignKey,
	func
)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
	__tablename__ = "users"
	id = Column(Integer, primary_key=True)
	name = Column(String)
