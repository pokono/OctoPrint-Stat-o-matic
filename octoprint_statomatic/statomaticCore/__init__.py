import sqlalchemy
from sqlalchemy import (
	create_engine,
	ForeignKey,
	Column,
	Integer,
	String,
	Float
)


class StatomaticCore(object):
	DIALECT = "sqlite"

	def __init__(self, config):
		# self.something = "yay"
		self.db_engine = create_engine("sqlite:///" + config.get("database.path"))
		self.db_connection = self.db_engine.connect()
		self.db_metadata = self.db_connection.MetaData()