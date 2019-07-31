from orator.migrations import Migration, SoftDeletes


class CreatePrintsTable(Migration, SoftDeletes):

	def up(self):
		"""
		Run the migrations.
		"""
		with self.schema.create("prints") as table:
			table.increments("id")
			table.string("name")
			table.string("path")
			table.string("origin")
			table.string("size")
			table.timestamps()
			table.softDeletes()

	def down(self):
		"""
		Revert the migrations.
		"""
		self.schema.drop("prints")
