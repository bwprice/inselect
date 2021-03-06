import unittest

from mock import patch

from PySide.QtGui import QMessageBox, QDialog

from gui_test import GUITest


class TestHelpBoxes(GUITest):
    """Help boxes are shown
    """
    @patch.object(QDialog, 'exec_', return_value=QDialog.Accepted)
    def test_help(self, mock_exec):
        "Help box is shown"
        self.window.help()

    @patch.object(QMessageBox, 'about', return_value=QMessageBox.Yes)
    def test_about(self, mock_exec):
        "Help box is shown"
        self.window.about()


if __name__=='__main__':
    unittest.main()
