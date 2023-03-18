from qgis.PyQt.QtWidgets import *
from .Impact_table_dialog import Ui_dlgImpacts


class DlgTable(QDialog, Ui_dlgImpacts):
    def __init__(self):
        super(DlgTable, self).__init__()
        self.setupUi(self)

        self.tblImpacts.setColumnWidth(0, 100)
        self.tblImpacts.setColumnWidth(1, 300)
