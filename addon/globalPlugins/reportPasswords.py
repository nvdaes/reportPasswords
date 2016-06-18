# reportPasswords: plugin to avoid keyboard echo suppressing on protected controls
# Settings managed with config.conf of NVDA
# Date: 15/06/2016
# Initial version
# Date: 16/04/2016

import addonHandler
import globalPluginHandler
import api
import controlTypes
import ui
import config
import wx
import gui
from gui import SettingsDialog
from globalCommands import SCRCAT_SPEECH, SCRCAT_CONFIG

addonHandler.initTranslation()

confspec = {
	"unprotectControls": "boolean(default=False)",
}

config.conf.spec["reportPasswords"] = confspec
isTypingProtected = api.isTypingProtected

def restoreIsProtected():
	api.isTypingProtected = isTypingProtected

def addonIsTypingProtected():
	if config.conf["reportPasswords"]["unprotectControls"]:
		return False
	focusObject = api.getFocusObject()
	if focusObject and (controlTypes.STATE_PROTECTED in focusObject.states or focusObject.role==controlTypes.ROLE_PASSWORDEDIT):
		return True

class AddonSettingsDialog(SettingsDialog):

	# Translators: title of a dialog.
	title = _("ReportPasswords settings")

	def makeSettings(self, settingsSizer):
		# Translators: label of a dialog.
		self.reportPasswordsCheckBox=wx.CheckBox(self, wx.NewId(), label=_("&Report passwords"))
		self.reportPasswordsCheckBox.SetValue(config.conf["reportPasswords"]["unprotectControls"])
		settingsSizer.Add(self.reportPasswordsCheckBox,border=10, flag=wx.BOTTOM)

	def postInit(self):
		self.reportPasswordsCheckBox.SetFocus()

	def onOk(self,evt):
		config.conf["reportPasswords"]["unprotectControls"] = self.reportPasswordsCheckBox.GetValue()
		super(AddonSettingsDialog, self).onOk(evt)

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self):
		super(globalPluginHandler.GlobalPlugin, self).__init__()
		api.isTypingProtected = addonIsTypingProtected
		self.prefsMenu = gui.mainFrame.sysTrayIcon.preferencesMenu
		self.settingsItem = self.prefsMenu.Append(wx.ID_ANY,
			# Translators: name of the option in the menu.
			_("&ReportPasswords settings..."),
			"")
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onSettings, self.settingsItem)

	def terminate(self):
		restoreIsProtected()
		try:
			self.prefsMenu.RemoveItem(self.settingsItem)
		except wx.PyDeadObjectError:
			pass

	def onSettings(self, evt):
		gui.mainFrame._popupSettingsDialog(AddonSettingsDialog)

	def script_settings(self, gesture):
		wx.CallAfter(self.onSettings, None)
	script_settings.category = SCRCAT_CONFIG
	# Translators: message presented in input help mode.
	script_settings.__doc__ = _("Shows the ReportPasswords settings dialog.")

	def script_toggleReportPasswords(self, gesture):
		config.conf["reportPasswords"]["unprotectControls"] = not config.conf["reportPasswords"]["unprotectControls"]
		if config.conf["reportPasswords"]["unprotectControls"]:
			ui.message(_("Report passwords on"))
		else:
			ui.message(_("Report passwords off"))
	script_toggleReportPasswords.category = SCRCAT_SPEECH
	# Translators: message presented in input help mode.
	script_toggleReportPasswords.__doc__ = _("Toggles on and off the speaking of text typed on protected controls as passwords.")

	__gestures = {
		"kb:NVDA+control+shift+p": "toggleReportPasswords",
	}
