from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont, QPalette, QColor
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5.QtWidgets import QGroupBox, QRadioButton
from PyQt5.QtWidgets import QPushButton, QLabel, QListWidget, QLineEdit

from instructions import *
from second_win import *
from final_win import *
     
class FirstScreen(QWidget):
    def __init__(self):
        super().__init__()

        # sets what the window will look like (label, size, location)
        self.set_appear()

        # creating and configuring graphic elements:
        self.initUI()

        #establishes connections between elements
        self.connects()

        # start:
        self.show()

    def initUI(self):
        self.btn_next = QPushButton(txt_next)
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.layout = QVBoxLayout()

        self.layout.addWidget(self.hello_text, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.instruction, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.btn_next, alignment = Qt.AlignCenter)   

        self.setLayout(self.layout)

    def next_click(self):
        self.hide()
        self.tw = TestWin()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    def set_appear(self):

        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

        self.setStyleSheet("""
            QWidget {
                background-color: #222222; 
                color: #FFFFFF;  
                font-size: 25px;
            }
            QLabel {
                font-size: 26px; 
                font-style: bold;
                                  
            }        
            QPushButton {
                background-color: #DFD0B8; 
                color: #000000; 
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #555555;  
            }         

        """)

        # second method
        # palette = self.palette()
        # palette.setColor(QPalette.Window, QColor(34, 34, 34))  
        # palette.setColor(QPalette.WindowText, QColor(255, 255, 255))  
        # self.setPalette(palette)
        
def main():
    app = QApplication([])
    mw = FirstScreen()
    app.exec_()

main()
