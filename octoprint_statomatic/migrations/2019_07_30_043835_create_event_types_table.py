from orator.migrations import Migration


class CreateEventTypesTable(Migration):

	def up(self):
		"""
		Run the migrations.
		"""
		with self.schema.create("event_types") as table:
			table.increments("id")
			table.string("event_type", 50).unique().index()
		# table.timestamps()

		self.db.table("event_types").insert([
			# Server
			{"event_type": "Startup"},
			{"event_type": "Shutdown"},
			{"event_type": "ClientOpened"},
			{"event_type": "ClientClosed"},
			{"event_type": "ConnectivityChanged"},
			# Printer Communication
			{"event_type": "Connecting"},
			{"event_type": "Connected"},
			{"event_type": "Disconnecting"},
			{"event_type": "Disconnected"},
			{"event_type": "Error"},
			{"event_type": "PrinterStateChanged"},
			# File Handling
			{"event_type": "Upload"},
			{"event_type": "FileAdded"},
			{"event_type": "FileRemoved"},
			{"event_type": "FolderAdded"},
			{"event_type": "FolderRemoved"},
			{"event_type": "UpdatedFiles"},
			{"event_type": "MetadataAnalysisStarted"},
			{"event_type": "MetadataAnalysisFinished"},
			{"event_type": "FileSelected"},
			{"event_type": "FileDeselected"},
			{"event_type": "TransferStarted"},
			{"event_type": "TransferDone"},
			# Printing
			{"event_type": "PrintStarted"},
			{"event_type": "PrintFailed"},
			{"event_type": "PrintDone"},
			{"event_type": "PrintCancelling"},
			{"event_type": "PrintCancelled"},
			{"event_type": "PrintPaused"},
			{"event_type": "PrintResumed"},
			# GCODE Processing
			{"event_type": "PowerOn"},
			{"event_type": "PowerOff"},
			{"event_type": "Home"},
			{"event_type": "ZChange"},
			{"event_type": "Dwell"},
			{"event_type": "Waiting"},
			{"event_type": "Cooling"},
			{"event_type": "Alert"},
			{"event_type": "Conveyor"},
			{"event_type": "Eject"},
			{"event_type": "EStop"},
			{"event_type": "PositionUpdate"},
			{"event_type": "ToolChange"},
			# Timelapses
			{"event_type": "CaptureStart"},
			{"event_type": "CaptureDone"},
			{"event_type": "CaptureFailed"},
			{"event_type": "MovieRendering"},
			{"event_type": "MovieDone"},
			{"event_type": "MovieFailed"},
			# Slicing
			{"event_type": "SlicingStarted"},
			{"event_type": "SlicingDone"},
			{"event_type": "SlicingCancelled"},
			{"event_type": "SlicingFailed"},
			{"event_type": "SlicingProfileAdded"},
			{"event_type": "SlicingProfileModified"},
			{"event_type": "SlicingProfileDeleted"},
			# Settings
			{"event_type": "SettingsUpdated"}
		])

	def down(self):
		"""
		Revert the migrations.
		"""
		self.schema.drop("event_types")
