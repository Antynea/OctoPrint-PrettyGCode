# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class PrettyGCodePlugin(octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.SettingsPlugin,
                       octoprint.plugin.AssetPlugin):
    def on_after_startup(self):
        self._logger.info("Pretty GCode.")
    pass
    def get_assets(self):
        return dict(
            js=["js/prettygcode.js","js/three.min.js",
                "js/LineSegmentsGeometry.js","js/LineGeometry.js","js/OBJLoader.js",
                "js/LineMaterial.js","js/LineSegments2.js","js/Line2.js","js/camera-controls.js","js/Lut.js","js/dat.gui.min.js"],
            css=["css/prettygcode.css"]
        )
# If you want your plugin to be registered within OctoPrint under a different name than what you defined in setup.py
# ("OctoPrint-PluginSkeleton"), you may define that here. Same goes for the other metadata derived from setup.py that
# can be overwritten via __plugin_xyz__ control properties. See the documentation for that.
__plugin_name__ = "PrettyGCode"
__plugin_implementation__ = PrettyGCodePlugin()
