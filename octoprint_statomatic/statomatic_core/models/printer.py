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


class Printer(Base):
	__tablename__ = "printers"
	id = Column(Integer, primary_key=True)
	identifier = Column(String, unique=True)
	name = Column(String)
	model = Column(String)
