
from PyQt5.QtWidgets import  QApplication



from firstwindow.start import StartWindow






app = QApplication([])

a  = StartWindow()
a.show()


app.exec()