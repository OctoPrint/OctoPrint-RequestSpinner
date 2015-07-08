# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class RequestSpinnerPlugin(octoprint.plugin.AssetPlugin, octoprint.plugin.TemplatePlugin):

	def get_assets(self):
		return dict(
			css=["css/requestspinner.css"],
			js=["js/requestspinner.js"],
			less=["less/requestspinner.less"]
		)

	##~~ Softwareupdate hook

	def get_update_information(self):
		return dict(
			requestspinner=dict(
				displayName="RequestSpinner Plugin",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="OctoPrint",
				repo="OctoPrint-RequestSpinner",
				current=self._plugin_version,

				# update method: pip w/ dependency links
				pip="https://github.com/OctoPrint/OctoPrint-RequestSpinner/archive/{target_version}.zip"
			)
		)

__plugin_name__ = "RequestSpinner"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = RequestSpinnerPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}
