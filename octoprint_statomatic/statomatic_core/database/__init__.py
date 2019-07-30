from orator import DatabaseManager, Model, SoftDeletes
from orator.exceptions.orm import ModelNotFound

from ...models.printer import Printer
from ...models.event_type import EventType
from ...models.event import Event

class Database(object):

	def __init__(self, config):
		self._db = DatabaseManager(config.get("database"))
		self._database_migrate(config.get("database.migrations_path"))
		Model.set_connection_resolver(self._db)


	def initialize(self):
		pass


	def store_printer(self, printer_profile):
		if printer_profile is None:
			return None

		printer = Printer.first_or_new(identifier=printer_profile["id"])
		printer.name = printer_profile["name"]
		printer.model = printer_profile["model"]
		printer.save()
		return printer

	def store_event(self, event_type, printer):
		if event_type is not None:
			try:
				type = EventType.where("event_type", "=", event_type).first_or_fail()
			except ModelNotFound:
				# Do nothing.
				print("ModelNotFound exeption")
				pass
			else:
				if printer is not None:
					Event.create(event_type=type.event_type, printer_identifier=printer.identifier)
				else:
					Event.create(event_type=type.event_type)

	####################
	# Utility methods. #
	####################

	# Migrate database programmatically.
	def _database_migrate(self, migrations_path):
		from orator.migrations import Migrator, DatabaseMigrationRepository

		repository = DatabaseMigrationRepository(self._db, 'migrations')
		migrator = Migrator(repository, self._db)  # db is the DatabaseManager instance

		if not migrator.repository_exists():
			repository.create_repository()

		# migrator.set_connection('pgsql')  # Needed only if it's not the default database
		migrator.run(migrations_path)  ## migrations_path is the directory where you migration files are
