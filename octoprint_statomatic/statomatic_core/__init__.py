from utils import Utils

from octoprint.events import Events

from .database import Database


class StatomaticCore(object):
	DIALECT = "sqlite"

	def __init__(self, config, logger):
		self._logger = logger
		self._database = Database(config)
		self._printer_profile = None
		self._printer = None

	def initialize(self):
		self._logger.debug("StatomaticCore initialize.")
		self._database.initialize()

	def event_connected(self, payload, printer_current_connection):
		# Payload:
		# port: the connected serial port
		# baudrate: the baud rate
		self._printer_profile = Utils.get_printer_profile(printer_current_connection)
		self._logger.debug("Printer connected - {pp}.".format(pp=dict(self._printer_profile)))
		self._printer = self._database.store_printer(self._printer_profile)

	def event_disconnected(self):
		# self._printer_profile = None
		# self._printer = None
		self._logger.debug("Printer disconnected.")

	def event_error(self, payload):
		# Payload:
		# error: the error string
		# self._printer_profile = None
		# self._printer = None
		self._logger.debug("Printer error.")

	def event_catch_all(self, event_type):
		if event_type is not Events.POWER_ON \
			and event_type is not Events.POWER_OFF \
			and event_type is not Events.HOME \
			and event_type is not Events.Z_CHANGE \
			and event_type is not Events.DWELL \
			and event_type is not Events.WAITING \
			and event_type is not Events.COOLING \
			and event_type is not Events.ALERT \
			and event_type is not Events.CONVEYOR \
			and event_type is not Events.EJECT \
			and event_type is not Events.E_STOP \
			and event_type is not Events.POSITION_UPDATE \
			and event_type is not Events.TOOL_CHANGE \
			and event_type is not Events.PRINTER_STATE_CHANGED:
			self._database.store_event(event_type, self._printer)

	def event_handle_printer_disconnect_and_error(self, event_type):
		if event_type is Events.DISCONNECTED or event_type is Events.ERROR:
			self._printer_profile = None
			self._printer = None
