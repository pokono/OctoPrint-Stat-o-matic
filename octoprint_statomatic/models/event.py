from orator import Model


class Event(Model):
	__table__ = "events"
	__primary_key__ = "id"
	# __dates__ = ['deleted_at']
	__fillable__ = ["event_type", "printer_identifier"]
# __guarded__ = ["id"]
