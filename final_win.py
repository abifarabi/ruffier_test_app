from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # checking the types of input values
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5.QtWidgets import QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from instructions import *

class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()

        #getting data about the experiment
        self.exp = exp

        # creating and configuring graphic elements:
        self.initUI()

        # sets what the window will look like (label, size, location)
        self.set_appear()
        
        # start:
        self.show()

    def results(self):
        if self.exp.age < 7:
            self.index = 0
            return "there is no data for this age"
        self.index = (4 * (int(self.exp.t1) + int(self.exp.t2) + int(self.exp.t3)) - 200) / 10
        if self.exp.age == 7 or self.exp.age == 8: # 7<= self.exp.age <= 8:
            if self.index >= 21:
                return txt_res1
            elif self.index < 21 and self.index >= 17:
                return txt_res2
            elif self.index < 17 and self.index >= 12:
                return txt_res3
            elif self.index < 12 and self.index >= 6.5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age == 9 or self.exp.age == 10:
            if self.index >= 19.5:
                return txt_res1
            elif self.index < 19.5 and self.index >= 15.5:
                return txt_res2
            elif self.index < 15.5 and self.index >= 10.5:
                return txt_res3
            elif self.index < 10.5 and self.index >= 5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age == 11 or self.exp.age == 12:
            if self.index >= 18:
                return txt_res1
            elif self.index < 18 and self.index >= 14:
                return txt_res2
            elif self.index < 14 and self.index >= 9:
                return txt_res3
            elif self.index < 9 and self.index >= 3.5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age == 13 or self.exp.age == 14:
            if self.index >= 16.5:
                return txt_res1
            elif self.index < 16.5 and self.index >= 12.5:
                return txt_res2
            elif self.index < 12.5 and self.index >= 7.5:
                return txt_res3
            elif self.index < 7.5 and self.index >= 2:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age >= 15:
            if self.index >= 15:
                return txt_res1
            elif self.index < 15 and self.index >= 11:
                return txt_res2
            elif self.index < 11 and self.index >= 6:
                return txt_res3
            elif self.index < 6 and self.index >= 0.5:
                return txt_res4
            else:
                return txt_res5
            
    def graph(self):
        figure = Figure(figsize=(5,4), facecolor='#222222')
        canvas = FigureCanvas(figure)
        ax = figure.add_subplot(111, facecolor='#222222')

        p1, p2, p3 = self.exp.t1, self.exp.t2, self.exp.t3
        ax.bar(['1st', '2nd', '3rd'], [p1, p2, p3], color=["#FFE033", "#10C43D", "#DA5059"])
        ax.set_ylabel('Pulse per 15 seconds')
        ax.set_title('Pulse Rate Comparison')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.spines['bottom'].set_color('white')
        ax.spines['left'].set_color('white')        
        ax.spines['top'].set_color("#FFF01A")  
        ax.yaxis.label.set_color('white')
        ax.title.set_color('white')

        ax.spines['right'].set_color('none')
        ax.set_ylim(0, max(p1, p2, p3) + 20)
        ax.grid(True, color='grey', linestyle='--', linewidth=0.5, alpha=0.5)
        return canvas

    def initUI(self):
        self.work_text = QLabel(txt_workheart + self.results())
        self.index_text = QLabel(txt_index + str(self.index))
        self.graph_canvas = self.graph()
        self.name_label = QLabel(f'Name: {self.exp.name}')
        self.age_label = QLabel(f'Age: {self.exp.age} years')


        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.work_text, alignment = Qt.AlignCenter) 
        self.layout_line.addWidget(self.graph_canvas, alignment = Qt.AlignCenter)
        self.layout_line.setAlignment(Qt.AlignCenter)       
        self.setLayout(self.layout_line)

    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
        self.setStyleSheet("""
            QWidget {
                background-color: #222222;  
                color: #FFFFFF;  
                font-size: 25px;
            }
                           
            QPushButton {
                background-color: #444444;  
                color: #FFFFFF;  
                border-radius: 5px;
                padding: 10px;
            }
                           
            QPushButton:hover {
                background-color: #555555;  
            }
        """)