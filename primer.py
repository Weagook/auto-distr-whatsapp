from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                            QLabel, QPushButton, QLineEdit, QTextEdit, QDateEdit,
                            QCalendarWidget, QMessageBox, QTimeEdit)
from PyQt5.QtCore import Qt, QDate, QTime, QDateTime
from PyQt5.QtGui import QFont
import json

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    
    def set_appear(self):
        self.setWindowTitle('Программа для работы с WhatsApp')
        self.resize(800, 600)

    def initUI(self):
        self.instr = QLabel('Выберите опцию')
        self.instr.setFont(QFont('Montserrat', 36, QFont.Bold))
        
        self.btn_newtask = QPushButton('Создать новую рассылку')
        self.btn_startbot = QPushButton('Запустить бота')
        self.btn_gettasks = QPushButton('Посмотреть запланированные задачи')
        
        self.main_l = QVBoxLayout()
        self.row1 = QHBoxLayout()
        self.row2 = QHBoxLayout()

        self.row1.addWidget(self.instr, alignment=Qt.AlignCenter)

        self.row2.addWidget(self.btn_newtask, alignment=Qt.AlignCenter)
        self.row2.addWidget(self.btn_startbot, alignment=Qt.AlignCenter)
        self.row2.addWidget(self.btn_gettasks, alignment=Qt.AlignCenter)
        
        self.main_l.addLayout(self.row1)
        self.main_l.addLayout(self.row2)

        self.setLayout(self.main_l)

    def connects(self):
        self.btn_newtask.clicked.connect(self.addTaskWindow)

    def addTaskWindow(self):
        self.tw = TaskWindow()

class TaskWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.selected_date = None

        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    
    def set_appear(self):
        self.setWindowTitle('Новая задача')
        self.resize(600, 400)
    
    def initUI(self):
        self.name_group = QLabel('Введите название группы')
        self.name_group.setFont(QFont('Montserrat', 18, QFont.Bold))
        self.nameGroupText = QLineEdit('')
        self.txt_message = QLabel('Текст перессылки')
        self.txt_message.setFont(QFont('Montserrat', 18, QFont.Bold))
        self.message = QTextEdit('')
        self.calendar_txt = QLabel('Выберите дату')
        self.calendar_txt.setFont(QFont('Montserrat', 18, QFont.Bold))
        self.calendar = QCalendarWidget()
        self.time_txt = QLabel('Выберите время')
        self.time_txt.setFont(QFont('Montserrat', 18, QFont.Bold))
        self.time_edit = QTimeEdit()
        self.time_edit.setTime(QTime.currentTime())
        self.button = QPushButton('Создать задачу')
        
        self.main_layout = QHBoxLayout()
        self.row1 = QVBoxLayout()
        self.row2 = QVBoxLayout()
        
        self.row1.addWidget(self.name_group, alignment=Qt.AlignLeft)
        self.row1.addWidget(self.nameGroupText, alignment=Qt.AlignLeft)
        self.row1.addWidget(self.txt_message, alignment=Qt.AlignLeft)
        self.row1.addWidget(self.message, alignment=Qt.AlignLeft)
        self.row1.addWidget(self.button, alignment=Qt.AlignRight)

        self.row2.addWidget(self.calendar_txt, alignment=Qt.AlignRight)
        self.row2.addWidget(self.calendar, alignment=Qt.AlignRight)
        self.row2.addWidget(self.time_txt, alignment=Qt.AlignRight)
        self.row2.addWidget(self.time_edit, alignment=Qt.AlignRight)

        self.main_layout.addLayout(self.row1)
        self.main_layout.addLayout(self.row2)
        
        self.setLayout(self.main_layout)

    def connects(self):
        self.calendar.clicked.connect(self.setDate)
        self.button.clicked.connect(self.check_data)
    
    def setDate(self, date):
        self.selected_date = {'year': date.year(), 'month': date.month(), 'day': date.day()}
    
    def check_data(self):
        print('Группа:', self.nameGroupText.text())
        print('Сообщение:', self.message.toPlainText())
        self.selected_time = {'hour': self.time_edit.time().hour(), 'minute': self.time_edit.time().minute()}
        print('Время:', self.selected_time)
        if self.selected_date:
            print('Дата:', self.selected_date)
        else:
            message_box = QMessageBox()
            message_box.setWindowTitle('Нет даты')
            message_box.setText('Выберите дату!')
            message_box.setIcon(QMessageBox.Information)
            message_box.setStandardButtons(QMessageBox.Ok)
            message_box.exec_()
        datetime = QDateTime(self.selected_date['year'], self.selected_date['month'], self.selected_date['day'], self.selected_time['hour'], self.selected_time['minute'])
        cur_datetime = QDateTime.currentDateTime()
        print(datetime)
        print(cur_datetime)
        print('Разница в секундах:', cur_datetime.secsTo(datetime))
        

if __name__ == "__main__":
    app = QApplication([])
    window = MainWin()
    app.exec()

