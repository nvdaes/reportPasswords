# -*- coding: UTF-8 -*-

# reportPasswords: plugin to avoid keyboard echo suppressing on protected controls
# Copyright (C) 2016-2022 Noelia Ruiz Martínez
# Released under GPL 2

import wx

import globalPluginHandler
import globalVars
import api
import config
import gui
from gui import SettingsPanel, NVDASettingsDialog, guiHelper
from scriptHandler import script
from globalCommands import SCRCAT_CONFIG
import addonHandler

addonHandler.initTranslation()

ADDON_SUMMARY = addonHandler.getCodeAddon().manifest["summary"]

confspec = {
	"unprotectControls": "boolean(default=False)"
}
config.conf.spec["reportPasswords"] = confspec

isTypingProtected = api.isTypingProtected


def restoreIsProtected():
	api.isTypingProtected = isTypingProtected


def addonIsTypingProtected():
	if config.conf["reportPasswords"]["unprotectControls"]:
		return False
	focus = api.getFocusObject()
	if focus.isProtected:
		return True


def disableInSecureMode(decoratedCls):
	if globalVars.appArgs.secure:
		return globalPluginHandler.GlobalPlugin
	return decoratedCls


class AddonSettingsPanel(SettingsPanel):

	title = ADDON_SUMMARY

	def makeSettings(self, settingsSizer):
		sHelper = guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		# Translators: label of a dialog.
		self.reportPasswordsCheckBox = sHelper.addItem(wx.CheckBox(self, label=_("&Report passwords")))
		self.reportPasswordsCheckBox.SetValue(config.conf["reportPasswords"]["unprotectControls"])

	def postInit(self):
		self.reportPasswordsCheckBox.SetFocus()

	def onSave(self):
		config.conf["reportPasswords"]["unprotectControls"] = self.reportPasswordsCheckBox.GetValue()


@disableInSecureMode
class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self):
		super(globalPluginHandler.GlobalPlugin, self).__init__()
		api.isTypingProtected = addonIsTypingProtected
		NVDASettingsDialog.categoryClasses.append(AddonSettingsPanel)

	def terminate(self):
		restoreIsProtected()
		NVDASettingsDialog.categoryClasses.remove(AddonSettingsPanel)

	def onSettings(self, evt):
		gui.mainFrame.popupSettingsDialog(NVDASettingsDialog, AddonSettingsPanel)

	@script(
		# Translators: Describes a command.
		description=_("Shows the %s settings.") % ADDON_SUMMARY,
		category=SCRCAT_CONFIG
	)
	def script_settings(self, gesture):
		wx.CallAfter(self.onSettings, None)
