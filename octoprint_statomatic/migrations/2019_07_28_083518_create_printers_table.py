from orator.migrations import Migration


class CreatePrintersTable(Migration):

	def up(self):
		"""
		Run the migrations.
		"""
		with self.schema.create("printers") as table:
			table.increments("id")
			table.string("identifier", 255).unique()
			table.string("name", 255)
			table.string("model", 255)
			table.timestamps()
			table.soft_deletes()

	def down(self):
		"""
		Revert the migrations.
		"""
		self.schema.drop("printers")
