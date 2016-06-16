# -*- coding: UTF-8 -*-
# Ask to remove the obsolete add-on settings, suggested by Rèmy Ruiz
# Date: 16/06/2016

import gui
import wx
import globalVars
import os
import addonHandler

addonHandler.initTranslation()

def onInstall():
	configFile = os.path.join(globalVars.appArgs.configPath, "reportPasswords.ini")
	if os.path.isfile(configFile):
		if gui.messageBox(
		# Translators: the label of a message box dialog.
		_("You seem to have previous settings saved for an old version of this add-on, and they should be removed. Do you want to remove them?"),
		# Translators: the title of a message box dialog.
		_("Remove obsolete add-on settings"),
		wx.YES|wx.NO|wx.ICON_WARNING)==wx.YES:
			try:
				os.remove(configFile)
			except WindowsError:
				pass
