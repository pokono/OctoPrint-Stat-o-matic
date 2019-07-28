from orator import Model, SoftDeletes


class Printer(Model, SoftDeletes):
	__table__ = "printers"
	__primary_key__ = "id"
	__dates__ = ['deleted_at']
	# __fillable__ = ["identifier", "name", "model"]
	__guarded__ = ["id"]
