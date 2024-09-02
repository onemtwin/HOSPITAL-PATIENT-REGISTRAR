#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
from PyQt5.QtWidgets import QApplication,QLabel,QLineEdit,QPushButton,QMainWindow,QWidget,QVBoxLayout
from PyQt5.QtGui import *
from PyQt5.QtCore import *


# In[3]:


class Patient_registration_app(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        
        # set up window
        self.setGeometry(100,200,300,400)
        self.setWindowTitle(" Patient Registrar")

        # add labels
        self.label0=QLabel(self)
        self.label0.setText("Patient Name : ")
        self.label0space=QLineEdit(self)
        

        self.label1=QLabel(self)
        self.label1.setText("Patient Age : ")
        self.label1space=QLineEdit(self)

        self.label2=QLabel(self)
        self.label2.setText("Patient Gender : ")
        self.label2space=QLineEdit(self)

        self.label3=QLabel(self)
        self.label3.setText("Patient Home Address : ")
        self.label3space=QLineEdit(self)

        self.label4=QLabel(self)
        self.label4.setText("Patient Health Condition")
        self.label4space=QLineEdit(self)

        self.label5=QLabel(self)
        self.label5.setText("Patient's Phone Number")
        self.label5space=QLineEdit(self)

        # set up the layout
        self.layout=QVBoxLayout()
        self.layout.addWidget(self.label0)
        self.layout.addWidget(self.label0space)
        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.label1space)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.label2space)
        self.layout.addWidget(self.label3)
        self.layout.addWidget(self.label3space)
        self.layout.addWidget(self.label4)
        self.layout.addWidget(self.label4space)
        self.layout.addWidget(self.label5)
        self.layout.addWidget(self.label5space)
        self.setLayout(self.layout)
        

if __name__=="__main__":
    app=QApplication(sys.argv)
    widget=Patient_registration_app()
    widget.show()
    sys.exit(app.exec_())


# In[ ]:




