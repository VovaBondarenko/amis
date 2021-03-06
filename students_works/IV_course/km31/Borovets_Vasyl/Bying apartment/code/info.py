# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'info.ui'
#
# Created: Fri Dec 23 23:18:29 2016
#      by: PyQt5 UI code generator 5.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from book_view import show_info
class Ui_information_page(object):
    def setupUi(self, information_page):
        self.inf = information_page
        info=show_info(self.title)


        information_page.setObjectName("information_page")
        information_page.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("hous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        information_page.setWindowIcon(icon)
        self.label_6 = QtWidgets.QLabel(information_page)
        self.label_6.setGeometry(QtCore.QRect(80, 10, 301, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.ok_but = QtWidgets.QPushButton(information_page)
        self.ok_but.setGeometry(QtCore.QRect(150, 250, 75, 23))
        self.ok_but.setObjectName("ok_but")
        self.label = QtWidgets.QLabel(information_page)
        self.label.setGeometry(QtCore.QRect(40, 53, 46, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(information_page)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 46, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(information_page)
        self.label_3.setGeometry(QtCore.QRect(40, 110, 46, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(information_page)
        self.label_4.setGeometry(QtCore.QRect(40, 140, 46, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(information_page)
        self.label_7.setGeometry(QtCore.QRect(40, 170, 46, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(information_page)
        self.label_8.setGeometry(QtCore.QRect(40, 200, 46, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.owner = QtWidgets.QLabel(information_page)
        self.owner.setGeometry(QtCore.QRect(90, 50, 281, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.owner.setFont(font)
        self.owner.setText(info[0][0])
        self.owner.setObjectName("owner")
        self.city = QtWidgets.QLabel(information_page)
        self.city.setGeometry(QtCore.QRect(90, 80, 281, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.city.setFont(font)
        self.city.setText(info[0][2])
        self.city.setObjectName("city")
        self.street = QtWidgets.QLabel(information_page)
        self.street.setGeometry(QtCore.QRect(90, 110, 281, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.street.setFont(font)
        self.street.setText(info[0][4])
        self.street.setObjectName("street")
        self.house = QtWidgets.QLabel(information_page)
        self.house.setGeometry(QtCore.QRect(90, 140, 281, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.house.setFont(font)
        self.house.setText(info[0][5])
        self.house.setObjectName("house")
        self.flat = QtWidgets.QLabel(information_page)
        self.flat.setGeometry(QtCore.QRect(90, 170, 281, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.flat.setFont(font)
        self.flat.setText(info[0][6])
        self.flat.setObjectName("flat")
        self.label_13 = QtWidgets.QLabel(information_page)
        self.label_13.setGeometry(QtCore.QRect(90, 200, 281, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setText(str(info[0][7]))
        self.label_13.setObjectName("label_13")
        self.label_9 = QtWidgets.QLabel(information_page)
        self.label_9.setGeometry(QtCore.QRect(40, 220, 46, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.email = QtWidgets.QLabel(information_page)
        self.email.setGeometry(QtCore.QRect(90, 220, 301, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.email.setFont(font)
        self.email.setText(info[0][1])
        self.email.setObjectName("email")
        self.retranslateUi(information_page)
        QtCore.QMetaObject.connectSlotsByName(information_page)
        self.ok_but.clicked.connect(self.button_click)

    def button_click(self):
        self.inf.close()


    def retranslateUi(self, information_page):
        _translate = QtCore.QCoreApplication.translate
        information_page.setWindowTitle(_translate("information_page", "Information page"))
        self.label_6.setText(_translate("information_page", "Information about apartment:"))
        self.ok_but.setText(_translate("information_page", "OK"))
        self.label.setText(_translate("information_page", "Owner:"))
        self.label_2.setText(_translate("information_page", "City   :"))
        self.label_3.setText(_translate("information_page", "Street:"))
        self.label_4.setText(_translate("information_page", "House:"))
        self.label_7.setText(_translate("information_page", "Flat   :"))
        self.label_8.setText(_translate("information_page", "Price :"))
        self.label_9.setText(_translate("information_page", "Email:"))

    def get_title(self, title):
        self.title = title


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    information_page = QtWidgets.QDialog()
    ui = Ui_information_page()
    ui.setupUi(information_page)
    information_page.show()
    sys.exit(app.exec_())

