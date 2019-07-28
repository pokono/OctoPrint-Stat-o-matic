class Utils(object):

	# Parse printer profile from _printer.get_current_connection()
	# https://docs.octoprint.org/en/master/modules/printer.html#octoprint.printer.PrinterInterface.get_current_connection
	#
	# (
	# 'Operational',
	# 'VIRTUAL',
	# 115200,
	# {
	# 	'heatedChamber': False,
	# 	'name': 'My Amazing Printer',
	# 	'color': 'default',
	# 	'axes': {
	# 		'y': {'speed': 6000, 'inverted': False},
	# 		'x': {'speed': 6000, 'inverted': False},
	# 		'z': {'speed': 200, 'inverted': False},
	# 		'e': {'speed': 300, 'inverted': False}
	# 	},
	# 	'heatedBed': True,
	# 	'volume': {'origin': 'lowerleft', 'formFactor': 'rectangular', 'depth': 200.0, 'width': 200.0, 'custom_box': False, 'height': 200.0},
	# 	'model': 'My Amazing Model',
	# 	'id': '_default',
	# 	'extruder': {'count': 1, 'nozzleDiameter': 0.4, 'offsets': [(0.0, 0.0)], 'sharedNozzle': False}
	# })
	@staticmethod
	def get_printer_profile(get_current_connection_result):
		printer_profile = get_current_connection_result[3]
		if printer_profile is None:
			return None
		else:
			return {
				"id": printer_profile["id"],
				"name": printer_profile["name"],
				"model": printer_profile["model"]
			}
