from orator import Model


class EventType(Model):
	__table__ = "event_types"
	__timestamps__ = False
	__primary_key__ = "id"
	# __dates__ = ['deleted_at']
	# __fillable__ = ["identifier", "name", "model"]
	__guarded__ = ["id"]
