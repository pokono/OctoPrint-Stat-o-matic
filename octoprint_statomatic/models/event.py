from orator import Model


class Event(Model):
	__table__ = "events"
	__primary_key__ = "id"
	# __dates__ = ['deleted_at']
	# __fillable__ = ["identifier", "name", "model"]
	__guarded__ = ["id"]
