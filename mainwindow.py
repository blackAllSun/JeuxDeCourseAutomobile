#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  mainwindow.py
#
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

UI_INFO = """
<ui>
  <menubar name='MenuBar'>
    <menu action='FileMenu'>
		<menu action='FileNew'/>
		<menu action='FileSave'/>
		<menu action='FileSaveAs'/>
		<menu action='FileOpen'/>
		<menu action='FilePrint'/>
      <separator />
      <menuitem action='FileQuit' />
    </menu>
    <menu action='EditMenu'>
		<menuitem action='EditCut' />
		<menuitem action='EditCopy' />
		<menuitem action='EditPaste' />
		<menuitem action='EditSuppr' />
    </menu>
    <menu action='MenuDialog'>
      <menuitem action='DialogAdresse'/>
      <menuitem action='DialogEcurie'/>
      <menuitem action='DialogVoiture'/>
      <menuitem action='DialogPilote'/>
      <menuitem action='DialogSponsor'/>
      <separator />
      <menuitem action='DialogContrat'/>
    </menu>
  </menubar>
  <toolbar name='ToolBar'>
    <toolitem action='FileNewStandard' />
    <toolitem action='FileSave'/>
	<toolitem action='FileSaveAs'/>
	<toolitem action='FileOpen'/>
	<toolitem action='FilePrint'/>
    <toolitem action='FileQuit' />
  </toolbar>
  <popup name='PopupMenu'>
	<menuitem action='EditCut' />
	<menuitem action='EditCopy' />
	<menuitem action='EditPaste' />
	<menuitem action='EditSuppr' />
  </popup>
</ui>
"""
class MainWindow(Gtk.Window):
	def __init__(self):
		Gtk.__init__(self,title="Jeux de Voiture Editeur")
		self.set_default_size(1024,840)
		actionGroup=Gtk.ActionGroup("my_actions")
		menubar = uimanager.get_widget("/MenuBar")
		box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		box.pack_start(menubar, False, False, 0)
        toolbar = uimanager.get_widget("/ToolBar")
        box.pack_start(toolbar, False, False, 0)
	
	def addFileMenuActions(self,actionGroup):
		actionFileMenu=Gtk.Action("FileMenu","File",None,None)
		actionGroup.add_action(actionFileMenu)
        actionFileNewMenu = Gtk.Action("FileNew", None, None, Gtk.STOCK_NEW)
        actionGroup.add_action(actionFileNewMenu)
        actionFileSaveMenu = Gtk.Action("FileSave", None, None, Gtk.STOCK_SAVE)
        actionGroup.add_action(actionFileSaveMenu)
        actionFileSaveAsMenu = Gtk.Action("FileSaveAs", None, None, Gtk.STOCK_SAVE_AS)
        actionGroup.add_action(actionFileSaveAsMenu)
        actionFileQuitMenu = Gtk.Action("FileQuit", None, None, Gtk.STOCK_QUIT)
        actionGroup.add_action(actionFileQuitMenu)
        actionFileQuitMenu.connect("activate", self.onMenuFileQuit)
        actionFileOpenMenu = Gtk.Action("FileOpen", None, None, Gtk.STOCK_OPEN)
        actionGroup.add_action(actionFileOpenMenu)
    def onMenuFileQuit(self, widget):
        Gtk.main_quit()
