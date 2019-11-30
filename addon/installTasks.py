# -*- coding: UTF-8 -*-

# Ask to remove the obsolete add-on settings, suggested by Rèmy Ruiz
# Date: 16/06/2016

import gui
import wx
import globalVars
import os
import config
import addonHandler

addonHandler.initTranslation()

confspec = {
	"unprotectControls": "boolean(default=False)"
}
config.conf.spec["reportPasswords"] = confspec

def onInstall():
	configFile = os.path.join(globalVars.appArgs.configPath, "reportPasswords.ini")
	if os.path.isfile(configFile):
		if gui.messageBox(
			# Translators: the label of a message box dialog.
			_("You seem to have previous settings saved for an old version of this add-on, and they should be removed. Do you want to remove them?"),
			# Translators: the title of a message box dialog.
			_("Remove obsolete add-on settings"),
			wx.YES|wx.NO|wx.ICON_WARNING
		)==wx.YES:
			try:
				os.remove(configFile)
			except WindowsError:
				pass
	if gui.messageBox(
		# Translators: the label of a message box dialog.
		_("If you want hear typed characters in protected controls like passwords, you need to enable the Report passwords option of this add-on and configure NVDA to speak typed characters. This may be useful just in certain situations, so you can create an NVDA's configuration profile for this. Do you want to set these options in a profile named reportPasswords with these settings now?"),
		# Translators: the title of a message box dialog.
		_("Set a dedicated profile for this add-on"),
		wx.YES|wx.NO|wx.ICON_QUESTION
	)==wx.YES:
		try:
			config.conf.createProfile("reportPasswords")
		except:
			pass
		config.conf.manualActivateProfile("reportPasswords")
		config.conf["reportPasswords"]["unprotectControls"] = True
		config.conf["keyboard"]["speakTypedCharacters"] = True
