# -*- coding: UTF-8 -*-

# installTasks for reportPasswords add-on
#Copyright (C) 2016-2019 Noelia Ruiz Martínez
# Released under GPL 2

import gui
import wx
import config
import addonHandler

addonHandler.initTranslation()

confspec = {
	"unprotectControls": "boolean(default=False)"
}
config.conf.spec["reportPasswords"] = confspec

def onInstall():
	if gui.messageBox(
		# Translators: the label of a message box dialog.
		_("If you want to hear typed characters in protected controls like passwords, you need to enable the Report passwords option of this add-on and configure NVDA to speak typed characters. This may be useful just in certain situations, so you can create an NVDA's configuration profile for this. Do you want to set these options in a profile named reportPasswords with these settings now?"),
		# Translators: the title of a message box dialog.
		_("Set a dedicated profile for this add-on"),
		wx.YES|wx.NO|wx.ICON_WARNING
	)==wx.YES:
		try:
			config.conf.createProfile("reportPasswords")
		except:
			pass
		config.conf.manualActivateProfile("reportPasswords")
		config.conf["reportPasswords"]["unprotectControls"] = True
		config.conf["keyboard"]["speakTypedCharacters"] = True
