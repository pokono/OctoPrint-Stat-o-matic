from utils import Utils

from .database import Database


class StatomaticCore(object):
	DIALECT = "sqlite"

	def __init__(self, config, logger):
		self._logger = logger
		self._database = Database(config)
		self._printer_profile = None

	def initialize(self):
		self._logger.debug("StatomaticCore initialize.")
		self._database.initialize()

	def event_connected(self, payload, printer_current_connection):
		# Payload:
		# port: the connected serial port
		# baudrate: the baud rate

		self._printer_profile = Utils.get_printer_profile(printer_current_connection)
		self._logger.debug("Printer connected - {pp}.".format(pp=dict(self._printer_profile)))
		self._database.store_printer(self._printer_profile)
		pass

	def event_disconnected(self):
		self._printer_profile = None
		self._logger.debug("Printer disconnected.")
		pass

	def event_error(self, payload):
		# Payload:
		# error: the error string
		self._printer_profile = None
		self._logger.debug("Printer error.")
		pass
