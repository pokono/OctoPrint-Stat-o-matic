from orator import DatabaseManager, Model, SoftDeletes

from ...models.printer import Printer

class Database(object):

	def __init__(self, config):
		self._db = DatabaseManager(config.get("database"))
		self._database_migrate(config.get("database.migrations_path"))
		Model.set_connection_resolver(self._db)


	def initialize(self):
		pass


	def store_printer(self, printer_profile):
		if printer_profile is None:
			return

		printer = Printer.first_or_new(identifier=printer_profile["id"])
		printer.name = printer_profile["name"]
		printer.model = printer_profile["model"]
		printer.save()

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
