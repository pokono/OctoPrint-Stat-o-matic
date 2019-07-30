from orator.migrations import Migration


class CreateEventTypeTable(Migration):

	def up(self):
		"""
		Run the migrations.
		"""
		with self.schema.create('event_type') as table:
			table.increments('id')
			table.string("event", 50).unique().index()
		# table.timestamps()

		self.db.table('event_type').insert([
			# Server
			{'event': 'Startup'},
			{'event': 'Shutdown'},
			{'event': 'ClientOpened'},
			{'event': 'ClientClosed'},
			{'event': 'ConnectivityChanged'},
			# Printer Communication
			{'event': 'Connecting'},
			{'event': 'Connected'},
			{'event': 'Disconnecting'},
			{'event': 'Disconnected'},
			{'event': 'Error'},
			{'event': 'PrinterStateChanged'},
			# File Handling
			{'event': 'Upload'},
			{'event': 'FileAdded'},
			{'event': 'FileRemoved'},
			{'event': 'FolderAdded'},
			{'event': 'FolderRemoved'},
			{'event': 'UpdatedFiles'},
			{'event': 'MetadataAnalysisStarted'},
			{'event': 'MetadataAnalysisFinished'},
			{'event': 'FileSelected'},
			{'event': 'FileDeselected'},
			{'event': 'TransferStarted'},
			{'event': 'TransferDone'},
			# Printing
			{'event': 'PrintStarted'},
			{'event': 'PrintFailed'},
			{'event': 'PrintDone'},
			{'event': 'PrintCancelling'},
			{'event': 'PrintCancelled'},
			{'event': 'PrintPaused'},
			{'event': 'PrintResumed'},
			# GCODE Processing
			{'event': 'PowerOn'},
			{'event': 'PowerOff'},
			{'event': 'Home'},
			{'event': 'ZChange'},
			{'event': 'Dwell'},
			{'event': 'Waiting'},
			{'event': 'Cooling'},
			{'event': 'Alert'},
			{'event': 'Conveyor'},
			{'event': 'Eject'},
			{'event': 'EStop'},
			{'event': 'PositionUpdate'},
			{'event': 'ToolChange'},
			# Timelapses
			{'event': 'CaptureStart'},
			{'event': 'CaptureDone'},
			{'event': 'CaptureFailed'},
			{'event': 'MovieRendering'},
			{'event': 'MovieDone'},
			{'event': 'MovieFailed'},
			# Slicing
			{'event': 'SlicingStarted'},
			{'event': 'SlicingDone'},
			{'event': 'SlicingCancelled'},
			{'event': 'SlicingFailed'},
			{'event': 'SlicingProfileAdded'},
			{'event': 'SlicingProfileModified'},
			{'event': 'SlicingProfileDeleted'},
			# Settings
			{'event': 'SettingsUpdated'}
		])

	def down(self):
		"""
		Revert the migrations.
		"""
		self.schema.drop('event_type')
