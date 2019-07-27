from alembic.config import Config
from alembic import command
from sqlalchemy import (
	create_engine,
	ForeignKey,
	Column,
	Integer,
	String,
	Float,
	func
)


class Database(object):

	def __init__(self, config):
		db_path = config.get("database.schema") + config.get("database.path")
		alembic_cfg_path = config.get("alembic.config.path")
		alembic_cfg_scriptlocation = config.get("alembic.config.scriptlocation")
		alembic_cfg = Config(alembic_cfg_path)
		alembic_cfg.set_main_option("script_location", alembic_cfg_scriptlocation)
		alembic_cfg.set_main_option("sqlalchemy.url", db_path)
		command.upgrade(alembic_cfg, "head")

		self._db_engine = create_engine(db_path)
		self._db_connection = None
		self._db_metadata = None

	def initialize(self):
		self._db_connection = self._db_engine.connect()
		self._db_metadata = self._db_connection.MetaData()
