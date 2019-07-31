from orator.migrations import Migration


class CreatePrintJobsTable(Migration):

	def up(self):
		"""
		Run the migrations.
		"""
		with self.schema.create("print_jobs") as table:
			table.increments("id")
			table.enum("print_status", [
				"Printing",
				"Paused",
				"Failed",
				"Done",
				"Cancelled"
			])
			table.integer("print_id")
			table.foreign("event_type").references("event_type").on("event_types")
			table.string("user").nullable()
			table.string("time_printed").nullable()
			table.string("failure_reason").nullable()
			table.string("failure_firmware_error").nullable()
			table.timestamps()

	def down(self):
		"""
		Revert the migrations.
		"""
		self.schema.drop("print_jobs")
