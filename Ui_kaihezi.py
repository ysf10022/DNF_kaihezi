# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kaihezi.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(344, 295)
        self.label = QLabel(widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(250, 30, 54, 12))
        self.label_2 = QLabel(widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(220, 50, 101, 51))
        self.label_3 = QLabel(widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(220, 110, 111, 41))
        self.label_4 = QLabel(widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(220, 160, 91, 41))
        self.label_5 = QLabel(widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(220, 205, 121, 31))
        self.label_6 = QLabel(widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 30, 54, 12))
        self.lineEdit = QLineEdit(widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 50, 113, 20))
        self.pushButton = QPushButton(widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 100, 131, 111))
        self.comboBox = QComboBox(widget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 250, 231, 22))
        self.label_7 = QLabel(widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 230, 54, 12))

        self.retranslateUi(widget)

        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"DNF\u5f00\u76d2\u5de5\u5177", None))
        self.label.setText(QCoreApplication.translate("widget", u"\u4f7f\u7528\u8bf4\u660e", None))
        self.label_2.setText(QCoreApplication.translate("widget", u"1.\u5c06\u6e38\u620f\u8c03\u621016:9,\n"
"1280X720\u5206\u8fa8\u7387\u3002\n"
"UI\u5927\u5c0f\u8bbe\u7f6e\u4e3a\u6700\u5c0f", None))
        self.label_3.setText(QCoreApplication.translate("widget", u"2.\u6253\u5f00\u7269\u54c1\u680f\uff0c\u5c06\u8981\n"
"\u5f00\u7684\u76d2\u5b50\u653e\u5728\u6d88\n"
"\u8017\u54c1\u7684\u7b2c\u4e00\u4e2a\u683c\u5b50", None))
        self.label_4.setText(QCoreApplication.translate("widget", u"3.\u8bbe\u7f6e\u5faa\u73af\u6b21\u6570\uff0c\n"
"\u9009\u62e9\u76d2\u5b50\u7c7b\u578b,\n"
"\u70b9\u51fb\u201c\u542f\u52a8!\u201d", None))
        self.label_5.setText(QCoreApplication.translate("widget", u"4.\u6309\u201cF10\u201d\u7ec8\u6b62\u5faa\u73af\n"
"(\u53ef\u80fd\u9700\u8981\u6309\u4e24\u6b21)", None))
        self.label_6.setText(QCoreApplication.translate("widget", u"\u5faa\u73af\u6b21\u6570", None))
        self.lineEdit.setText(QCoreApplication.translate("widget", u"1", None))
        self.pushButton.setText(QCoreApplication.translate("widget", u"\u542f\u52a8\uff01", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("widget", u"\u81ea\u5b9a\u4e49\u76d2\u5b50/3\u8bcd\u6761\u56fa\u5b9a\u76d2\u5b50-\u5f00\u4e0a\u8863", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("widget", u"\u4e07\u8c61\u56fa\u5b9a\u76d2\u5b50-\u5f00\u5de8\u5251", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("widget", u"\u81ea\u5b9a\u4e49\u76d2\u5b50/3\u8bcd\u6761\u56fa\u5b9a\u76d2\u5b50-\u5f00\u4e0a\u8863", None))
        self.label_7.setText(QCoreApplication.translate("widget", u"\u76d2\u5b50\u7c7b\u578b", None))
    # retranslateUi

