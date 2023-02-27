from PyQt5 import QtWidgets, QtCore, QtGui

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.p = None

        self.btn = QtWidgets.QPushButton("Comenzar",self)
        self.btn.pressed.connect(self.start_process)
        self.btn_finalizar = QtWidgets.QPushButton("Finalizar", self)
        self.btn_finalizar.pressed.connect(self.close)
        self.text = QtWidgets.QPlainTextEdit()
        self.text.setReadOnly(True)

        l = QtWidgets.QVBoxLayout()
        l.addWidget(self.text)
        h = QtWidgets.QHBoxLayout()
        h.addWidget(self.btn)
        h.addWidget(self.btn_finalizar)
        l.addLayout(h)
        w = QtWidgets.QWidget()
        w.setLayout(l)

        self.setWindowTitle("Window for testing")
        self.setCentralWidget(w)
        self.setFixedSize(QtCore.QSize(400, 450))
        self.setMinimumSize(QtCore.QSize(250, 350))
        self.setMaximumSize(QtCore.QSize(800, 950))
        self.setWindowIcon(QtGui.QIcon('icon.png'))

    def message(self, s):
        self.text.appendPlainText(s)

    def start_process(self):
        if self.p is None:
            self.message("Executing process")
            self.p = QtCore.QProcess()
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)
            self.p.start("pytest", ['test5.py'])

    def handle_stderr(self):
        data = self.p.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        self.message(stderr)

    def handle_stdout(self):
        data = self.p.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.message(stdout)

    def handle_state(self, state):
        states = {
            QtCore.QProcess.NotRunning: 'Not running',
            QtCore.QProcess.Starting: 'Starting',
            QtCore.QProcess.Running: 'Running',
        }
        state_name = states[state]
        self.message(f"State changed: {state_name}")

    def process_finished(self):
        self.message("Process finished.")
        self.p = None

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
