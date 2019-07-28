# coding=utf-8
from __future__ import absolute_import

### (Don't forget to remove me)
# This is a basic skeleton for your plugin's __init__.py. You probably want to adjust the class name of your plugin
# as well as the plugin mixins it's subclassing from. This is really just a basic skeleton to get you started,
# defining your plugin as a template plugin, settings and asset plugin. Feel free to add or remove mixins
# as necessary.
#
# Take a look at the documentation on what other plugin mixins are available.

import os

import octoprint.plugin
from octoprint.printer import PrinterInterface
from octoprint.events import Events
from .statomatic_core import StatomaticCore


class StatomaticPlugin(octoprint.plugin.StartupPlugin,
					   octoprint.plugin.SettingsPlugin,
					   octoprint.plugin.AssetPlugin,
					   octoprint.plugin.TemplatePlugin,
					   octoprint.plugin.EventHandlerPlugin):

	def __init__(self):
		self._config = None
		self._statomatic_core = None


	def initialize(self):
		self._config = {
			"database.schema": "sqlite:///",
			"database.path": os.path.join(self.get_plugin_data_folder(), "stat-o-matic.sqlite"),
			"alembic.config.path": "./octoprint_statomatic/alembic.ini",
			"alembic.config.scriptlocation": "./octoprint_statomatic/alembic",
		}
		# db_schema = 'sqlite:///'
		# db_path = os.path.join(self.get_plugin_data_folder(), "stat-o-matic.sqlite")
		# alembic_cfg = Config("./octoprint_statomatic/alembic.ini")
		# alembic_cfg.set_main_option("script_location", "./octoprint_statomatic/alembic")
		# alembic_cfg.set_main_option("sqlalchemy.url", db_schema + db_path)
		# command.upgrade(alembic_cfg, "head")
		self._statomatic_core = StatomaticCore(self._config, self._logger)
		self._statomatic_core.initialize()
		print(self._user_manager.enabled)
		print (self._user_manager.getAllUsers())

	# self.database = Database.initialize(self.config)

	##~~ EventHandlerPlugin mixin

	def on_event(self, event, payload):
		# listening_events = {
		# 	Events.CONNECTED: self._statomatic_core.event_connected(payload, self._printer.get_current_connection()),
		# 	Events.DISCONNECTED: self._statomatic_core.event_disconnected(),
		# 	Events.ERROR: self._statomatic_core.event_error(payload)
		# }
		# try:
		# 	listening_events[event]()
		# except:
		# 	print (event)
		# 	pass
		if event == Events.CONNECTED:
			connection = self._printer.get_current_connection()
			self._statomatic_core.event_connected(payload, connection)

		elif event == Events.DISCONNECTED:
			self._statomatic_core.event_disconnected()

		elif event == Events.ERROR:
			self._statomatic_core.event_error(payload)


	##~~ SettingsPlugin mixin

	def get_settings_defaults(self):
		return dict(
			# put your plugin's default settings here
			url="https://ivancarosati.com"
		)

	##~~ TemplatePlugin mixin

	# def get_template_vars(self):
	# 	return dict(
	# 		url=self._settings.get(["url"])
	# 	)\

	# The reason for this is that OctoPrint by default assumes that you’ll want to
	# bind your own view models to your templates and hence “unbinds” the included
	# templates from the templates that are in place at the injected location already.
	# In order to tell OctoPrint to please don’t do this here (since we do want to use
	# both NavigationViewModel and SettingsViewModel), we’ll need to override the default
	# template configuration using the get_template_configs method.
	# We’ll tell OctoPrint to use no custom bindings for both our navbar and our settings plugin.
	def get_template_configs(self):
		return [
			dict(type="navbar", custom_bindings=False),
			dict(type="settings", custom_bindings=False)
		]

	##~~ AssetPlugin mixin

	def get_assets(self):
		# Define your plugin's asset files to automatically include in the
		# core UI here.
		return dict(
			js=["js/statomatic.js"],
			css=["css/statomatic.css"],
			less=["css/statomatic.less"]
		)

	##~~ Softwareupdate hook

	def get_update_information(self):
		# Define the configuration for your plugin to use with the Software Update
		# Plugin here. See https://github.com/foosel/OctoPrint/wiki/Plugin:-Software-Update
		# for details.
		return dict(
			stat_o_matic=dict(
				displayName="Stat-o-matic Plugin",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="pokono",
				repo="OctoPrint-Stat-o-matic",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/pokono/OctoPrint-Stat-o-matic/archive/{target_version}.zip"
			)
		)


# If you want your plugin to be registered within OctoPrint under a different name than what you defined in setup.py
# ("OctoPrint-PluginSkeleton"), you may define that here. Same goes for the other metadata derived from setup.py that
# can be overwritten via __plugin_xyz__ control properties. See the documentation for that.
__plugin_name__ = "Stat-o-matic Plugin"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = StatomaticPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}

