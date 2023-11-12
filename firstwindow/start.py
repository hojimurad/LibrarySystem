


from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QMainWindow, QFormLayout, QVBoxLayout, QLineEdit,QPushButton
from PyQt5.QtCore import Qt

class StartMEnuWindow(QMainWindow):

    def __init__(self):
        super().__init__()


        self.setWindowTitle("Menu panel")

class StartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.srMenu =False
        self.setWindowTitle("Kirish paneli")
        """user property"""
        self.password = ["najot","1230"]
        self.setMinimumSize(800,500)


        self.vl = QVBoxLayout()

        self.ql =QLabel("Tizmga hush kelibsiz")
        self.ql.setAlignment(Qt.AlignCenter)
        font = self.ql.font()
        font.setBold(True)
        font.setPointSize(25)
        self.ql.setFont(font)


        self.passLabel  =QLabel("Enter your pasword")

        self.qe =QLineEdit()
        self.qe.setPlaceholderText("Enter your pasword")
        self.sub_l = QLabel()
        self.btn  =QPushButton("Ok")

        self.vl.addWidget(self.ql)

        self.vl.addWidget(self.passLabel)
        self.vl.addWidget(self.qe)
        self.vl.addWidget(self.btn)

        w = QWidget()
        w.setLayout(self.vl)
        self.setCentralWidget(w)

        self.btn.clicked.connect(self.the_btn)

    def the_btn(self):
        if self.qe.text() in self.password:
            self.passLabel.setText("correct")
            self.srMenu = StartMEnuWindow()
            self.srMenu.show()
        else:
            self.passLabel.text("try again")