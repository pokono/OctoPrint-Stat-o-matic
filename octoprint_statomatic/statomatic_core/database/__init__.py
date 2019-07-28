# from alembic.config import Config
# from alembic import command
# from sqlalchemy import (
# 	create_engine,
# 	ForeignKey,
# 	Column,
# 	Integer,
# 	String,
# 	Float,
# 	func
# )
# from sqlalchemy.orm import (
# 	sessionmaker,
# 	relationship
# )
# from sqlalchemy.ext.declarative import declarative_base
#
# from ..models.user import User
# from ..models.printer import Printer

# Base = declarative_base()

from orator import DatabaseManager, Model

from ...models.printer import Printer

class Database(object):

	def __init__(self, config):
		# db_path = config.get("database.schema") + config.get("database.path")
		# alembic_cfg_path = config.get("alembic.config.path")
		# alembic_cfg_scriptlocation = config.get("alembic.config.scriptlocation")
		# alembic_cfg = Config(alembic_cfg_path)
		# alembic_cfg.set_main_option("script_location", alembic_cfg_scriptlocation)
		# alembic_cfg.set_main_option("sqlalchemy.url", db_path)
		# command.upgrade(alembic_cfg, "head")
		#
		# self._db_engine = create_engine(db_path)
		# self._db_session = None
		self._db = DatabaseManager(config.get("database"))
		self.database_migrate(config.get("database.migrations_path"))
		Model.set_connection_resolver(self._db)


	def initialize(self):
		print("Database - Init")
		# self._db_connection = self._db_engine.connect()
		# self._db_metadata = self._db_connection.MetaData()
		# self._db_session = sessionmaker(bind=self._db_engine)
		# session = sessionmaker()
		# session.configure(bind=self._db_engine)
		# Base.metadata.bind = self._db_engine
		self.test_create_record()

	def test_create_record(self):
		# print("test_create_record called")
		# session = self.create_new_session()
		# print("session created")
		# pokono = User(name="Pokono")
		# print("pokono created")
		# session.add(pokono)
		# print("session add")
		# session.commit()
		# print("pokono: ")
		# print(pokono.id)
		# session.close()
		# print("New user committed.")
		pass

	def store_printer(self, printer_profile):
		if printer_profile is None:
			return

		# session = self.create_new_session()
		# printer = Printer(indentifier=printer_profile["id"],
		# 				  name=printer_profile["name"],
		# 				  model=printer_profile["model"])
		# session.add(printer)
		# session.commit()
		printer = Printer.first_or_new(identifier=printer_profile["id"])
		printer.name = printer_profile["name"]
		printer.model = model = printer_profile["model"]
		printer.save()


	# Utilities - Create a new database session.
	# def create_new_session(self):
	# 	return self._db_session()

	def database_migrate(self, migrations_path):
		from orator.migrations import Migrator, DatabaseMigrationRepository

		repository = DatabaseMigrationRepository(self._db, 'migrations')
		migrator = Migrator(repository, self._db)  # db is the DatabaseManager instance

		if not migrator.repository_exists():
			repository.create_repository()

		# migrator.set_connection('pgsql')  # Needed only if it's not the default database
		migrator.run(migrations_path)  ## migrations_path is the directory where you migration files are
