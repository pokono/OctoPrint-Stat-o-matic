import sqlalchemy
from sqlalchemy import (
	create_engine,
	ForeignKey,
	Column,
	Integer,
	String,
	Float,
	func,
	label
)


class Database(object):

	def __init__(self, config):
		self.config = config
		self.db_engine = None
		self.db_connection = None
		self.db_metadata = None

	def initialize(self, config):
		self.db_engine = create_engine("sqlite:///" + config.get("database.path"))
		self.db_connection = self.db_engine.connect()
		self.db_metadata = self.db_connection.MetaData()
