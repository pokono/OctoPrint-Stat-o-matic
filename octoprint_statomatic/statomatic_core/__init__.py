from utils import Utils

from .database import Database


class StatomaticCore(object):
	DIALECT = "sqlite"

	def __init__(self, config, logger):
		# self.something = "yay"
		# self.db_engine = create_engine("sqlite:///" + config.get("database.path"))
		# self.db_connection = self.db_engine.connect()
		# self.db_metadata = self.db_connection.MetaData()
		print("StatomaticCore init.")
		print(config)
		self._logger = logger
		self._database = Database(config)
		self._printer_profile = None

	def initialize(self):
		self._database.initialize()

	def event_connected(self, payload, printer_current_connection):
		# Payload:
		# port: the connected serial port
		# baudrate: the baud rate
		self._printer_profile = Utils.get_printer_profile(printer_current_connection)
		# self._logger.debug("Printer connected - {printer_profile}").format(printer_profile=dict(self._printer_profile))
		print (payload)
		print(self._printer_profile)
		self._database.store_printer(self._printer_profile)
		pass

	def event_disconnected(self):
		pass

	def event_error(self, payload):
		# Payload:
		# error: the error string
		pass
