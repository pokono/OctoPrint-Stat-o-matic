from orator.migrations import Migration


class CreateEventsTable(Migration):

	def up(self):
		"""
		Run the migrations.
		"""
		with self.schema.create("events") as table:
			table.increments("id")
			table.string("event_type", 50)
			table.foreign("event_type").references("event_type").on("event_types")
			table.timestamps()

	def down(self):
		"""
		Revert the migrations.
		"""
		self.schema.drop("events")
