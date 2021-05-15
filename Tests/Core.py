
import sys

from PyQt5.QtWidgets import QApplication

from Modules.View import GraphUI
from Modules.Model import GraphModel
from Modules.Control import GraphCtrl


def main():
	app = QApplication(sys.argv)

	view = GraphUI()

	model = GraphModel()

	GraphCtrl(model, view)

	view.show()
	sys.exit(app.exec())

if __name__ == "__main__":
	main()

