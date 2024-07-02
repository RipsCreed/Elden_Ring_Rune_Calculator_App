from PyQt5 import QtCore, QtGui, QtWidgets
import math


class Ui_calculator(object):
    def setupUi(self, calculator):
        calculator.setObjectName("calculator")
        calculator.resize(561, 298)
        self.label = QtWidgets.QLabel(calculator)
        self.label.setGeometry(QtCore.QRect(10, 60, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Level2 = QtWidgets.QLineEdit(calculator)
        self.Level2.setGeometry(QtCore.QRect(390, 130, 113, 31))
        self.Level2.setObjectName("Level2")
        self.label_3 = QtWidgets.QLabel(calculator)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.required_rune = QtWidgets.QLabel(calculator)
        self.required_rune.setGeometry(QtCore.QRect(10, 180, 541, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.required_rune.setFont(font)
        self.required_rune.setText("")
        self.required_rune.setObjectName("required_rune")
        self.label_2 = QtWidgets.QLabel(calculator)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 791, 51))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("text-align: center;")
        self.label_2.setObjectName("label_2")
        self.calculate_button = QtWidgets.QPushButton(calculator)
        self.calculate_button.setGeometry(QtCore.QRect(10, 220, 541, 61))
        self.calculate_button.setObjectName("calculate_button")
        font1 = QtGui.QFont()
        font1.setPointSize(20)
        self.calculate_button.setFont(font1)
        self.Level1 = QtWidgets.QLineEdit(calculator)
        self.Level1.setGeometry(QtCore.QRect(390, 70, 113, 31))
        self.Level1.setObjectName("Level1")
        
        self.calculate_button.clicked.connect(self.Click)

        self.retranslateUi(calculator)
        QtCore.QMetaObject.connectSlotsByName(calculator)
        
    def Click(self):
        self.lvl = int(self.Level1.text())
        
        self.lvl_to = int(self.Level2.text())
        
        total_rune_cost = 0
        
        y = int(self.lvl_to) - int(self.lvl)

        
        for i in range(y):
            
            total_rune_cost += self.Calculate_Rune()
            self.lvl += 1
            
        
        self.required_rune.setText("Required rune is " + str(math.ceil(total_rune_cost)))
        
    def Calculate_Rune(self):
        if ((self.lvl + 81) - 92) * 0.02 < 0:
            x = 0
        else:
            x = ((self.lvl + 81) - 92) * 0.02
        
        Rune_Cost = math.floor(((x + 0.1) * ((self.lvl+81) ** 2)) + 1)

        return Rune_Cost

    def retranslateUi(self, calculator):
        _translate = QtCore.QCoreApplication.translate
        calculator.setWindowTitle(_translate("calculator", "Elden Ring Rune Calculator"))
        self.label.setText(_translate("calculator", "Enter Your Level"))
        self.label_3.setText(_translate("calculator", "Enter Desired Level"))
        self.label_2.setText(_translate("calculator", "Elden Ring Rune Calculator"))
        self.calculate_button.setText(_translate("calculator", "Calculate"))
        
if __name__ == "__main__":
    import sys
    app= QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_calculator()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
