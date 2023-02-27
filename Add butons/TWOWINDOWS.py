from PyQt5 import QtWidgets, QtGui, QtCore
import PROCESS


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.window_2 = PROCESS.MainWindow()
        self.setAcceptDrops(True)
        self.resize(600, 500)
        self.main_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.vertical_layout = QtWidgets.QVBoxLayout(self.main_widget)
        self.frame = QtWidgets.QFrame(self.main_widget)
        self.horizontal_layout = QtWidgets.QHBoxLayout(self.frame)
        self.line_edit = QtWidgets.QLineEdit(self.main_widget)
        self.push_button = QtWidgets.QPushButton('Browse', self.frame)
        self.push_buttonNext = QtWidgets.QPushButton('Iniciar Test', self.main_widget)
        self.push_buttonClose = QtWidgets.QPushButton('Close', self.main_widget)
        self.push_button.setStyleSheet("color:black; ")
        self.push_buttonNext.setStyleSheet("background-color: green; color: white;")
        self.push_buttonClose.setStyleSheet("background-color: red; color: white;")
        self.horizontal_layout.addWidget(self.line_edit)
        self.horizontal_layout.addWidget(self.push_button)
        self.vertical_layout.addWidget(self.frame)
        self.text_edit = QtWidgets.QTextEdit(self.main_widget)
        self.bottom_buttons_layout = QtWidgets.QHBoxLayout()
        self.push_button_2 = QtWidgets.QPushButton('O arrastra aquí', self.main_widget)
        self.push_button_2.setStyleSheet("color:black; ")
        self.bottom_buttons_layout.addWidget(self.push_button_2)
        self.bottom_buttons_layout.addWidget(self.push_buttonClose)
        self.bottom_buttons_layout.addWidget(self.push_buttonNext)
        self.bottom_buttons_layout.addStretch()
        self.vertical_layout.addWidget(self.text_edit)
        self.vertical_layout.addLayout(self.bottom_buttons_layout)
        self.push_button.clicked.connect(self.open_file_dialog)
        self.push_buttonNext.clicked.connect(self.show_process)
        self.push_buttonClose.clicked.connect(self.close)
        self.push_button_2.clicked.connect(self.open_file)

        # contador de lineas
        self.line_count_label = QtWidgets.QLabel(self.main_widget)
        self.line_count_label.setAlignment(QtCore.Qt.AlignRight)
        self.vertical_layout.addWidget(self.line_count_label)

        self.text_edit.textChanged.connect(self.update_line_count)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            file_path = str(url.toLocalFile())
            self.load_file(file_path)

    def load_file(self, file_path):
        with open(file_path, 'r') as f:
            self.text_edit.setPlainText(f.read())

    def open_file_dialog(self):
        self.file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self,
                                                                   caption="Open Text File",
                                                                   directory="",
                                                                   filter="Python Files (*.py)",
                                                                   options=QtWidgets.QFileDialog.DontUseNativeDialog)
        if self.file_name:
            self.line_edit.setText(self.file_name)


    def open_file(self):
        with open(self.file_name, 'r') as f:
            self.text_edit.setPlainText(f.read())

    def show_process(self):
        if self.text_edit.toPlainText() == "":
            QtWidgets.QMessageBox.warning(self, "Advertencia", "Por favor carga un archivo antes de continuar.")
        else:
            
            self.window_2.text.setPlainText(self.text_edit.toPlainText())
            self.window_2.setWindowModality(QtCore.Qt.ApplicationModal)  # bloquear la ventana principal
            self.window_2.show()

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, 'Cerrar',
            "¿Estás seguro de salir?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def update_line_count(self):
        line_count = self.text_edit.document().blockCount()
        self.line_count_label.setText(f"Líneas: {line_count}")



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationDisplayName("Example")
    ui = MainWindow()
    ui.show()
    app.exec_()
