from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QWidget, QFileDialog
from PyQt5.QtGui import  QPixmap


import matplotlib.pyplot as plt


class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("AFTER LIGHT INSIGHT")
        MainWindow.resize(809, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setStyleSheet("color: white;""background-color: #222840;")

        ############################# fonts #######################


        font_bl = QtGui.QFont()
        font_bl.setPointSize(12)
        font_bl.setBold(True)
        font_bl.setWeight(75)

        ### Browse Button  ######
        bbt_font = QtGui.QFont()
        bbt_font.setPointSize(9)
        bbt_font.setBold(True)
        bbt_font.setWeight(75)
        
        #### all Buttons   #####
        bt_font = QtGui.QFont()
        bt_font.setPointSize(12)
        bt_font.setBold(True)
        bt_font.setWeight(75)
        



        ################################### frames ##################################

        self.browse_frame = QtWidgets.QFrame(self.centralwidget)
        self.browse_frame.setGeometry(QtCore.QRect(1, 0, 800, 49))
        self.browse_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.browse_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.browse_frame.setObjectName("browse_frame")
        self.browse_frame.setAutoFillBackground(True)

        self.browse_frame.setStyleSheet("color: white;" "selection-color: red;""selection-background-color: blue;")

        
        self.input_frame = QtWidgets.QFrame(self.centralwidget)
        self.input_frame.setGeometry(QtCore.QRect(5, 50, 390, 400))
        self.input_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.input_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.input_frame.setObjectName("input_frame")
        

        self.out_frame = QtWidgets.QFrame(self.centralwidget)
        self.out_frame.setGeometry(QtCore.QRect(400, 50, 400, 400))
        self.out_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.out_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.out_frame.setObjectName("out_frame")
        

        self.text_frame = QtWidgets.QFrame(self.centralwidget)
        self.text_frame.setGeometry(QtCore.QRect(1, 450, 800, 250))
        self.text_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.text_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.text_frame.setObjectName("text_frame")
        


                            ########################## Buttons ####################################

        ############ Browse ##########
        
        self.browse_bt= QtWidgets.QToolButton(self.browse_frame)
        self.browse_bt.setGeometry(QtCore.QRect(644, 2, 90, 31))
        self.browse_bt.setObjectName("browse_bt")
        self.browse_bt.setFont(bbt_font)
        directory = self.browse_bt.clicked.connect(self._open_file_dialog)
        self.browse_bt.setStyleSheet("color: white;""background-color: grey;" )



        ######################### Enhance_bt ##################
        self.Enhance_bt = QtWidgets.QPushButton(self.text_frame)
        self.Enhance_bt.setGeometry(QtCore.QRect(0, 1, 130, 57))
        self.Enhance_bt.setObjectName("Enhance_bt")
        self.Enhance_bt.clicked.connect(self.Enhance)
        self.Enhance_bt.setFont(bt_font)
        self.Enhance_bt.setStyleSheet("color: white;""background-color: grey;" )


        ######################### Save_bt ##################
        self.Save_bt = QtWidgets.QPushButton(self.text_frame)
        self.Save_bt.setGeometry(QtCore.QRect(0, 172, 130, 62))
        self.Save_bt.setObjectName("Save_bt")
        self.Save_bt.clicked.connect(self.Save)
        self.Save_bt.setFont(bt_font)
        self.Save_bt.setStyleSheet("color: white;""background-color: grey;" )


        ######################### text_bt ##################
        self.text_bt = QtWidgets.QPushButton(self.text_frame)
        self.text_bt.setGeometry(QtCore.QRect(0, 58, 130, 57))
        self.text_bt.setObjectName("text_bt")
        self.text_bt.clicked.connect(self.getText)
        self.text_bt.setFont(bt_font)
        self.text_bt.setStyleSheet("color: white;""background-color: grey;" )


        ######################### hist_bt ##################
        self.hist_bt = QtWidgets.QPushButton(self.text_frame)
        self.hist_bt.setGeometry(QtCore.QRect(0, 115, 130, 57))
        self.hist_bt.setObjectName("hist_bt")
        self.hist_bt.clicked.connect(self.show_hist)
        self.hist_bt.setFont(bt_font)
        self.hist_bt.setStyleSheet("color: white;""background-color: grey;" )


        # ############### text browser ##################

        self.textBrowser = QtWidgets.QLineEdit(self.browse_frame)
        self.textBrowser.setEnabled(False)
        self.textBrowser.setGeometry(QtCore.QRect(140,3, 500, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setText('')

    
        ################################## labels   ###################

        self.browse_lable = QtWidgets.QLabel(self.browse_frame)
        self.browse_lable.setGeometry(QtCore.QRect(6, 4, 111, 31))
        self.browse_lable.setFont(font_bl)
        self.browse_lable.setObjectName("browse_lable")

       

        self.input_label = QtWidgets.QLabel(self.input_frame)
        self.input_label.setGeometry(QtCore.QRect(150, 1, 110, 25))
        self.input_label.setAutoFillBackground(True)
        self.input_label.setScaledContents(True)
        self.input_label.setText("input_img")
        self.input_label.setObjectName("input_img")
        self.input_label.setFont(font_bl)

        self.out_label = QtWidgets.QLabel(self.out_frame)
        self.out_label.setGeometry(QtCore.QRect(150, 1, 110, 25))
        self.out_label.setAutoFillBackground(True)
        self.out_label.setScaledContents(True)
        self.out_label.setText("output Image")
        self.out_label.setObjectName("out_img")
        self.out_label.setFont(font_bl)


        self.input_img = QtWidgets.QLabel(self.input_frame)
        self.input_img.setGeometry(QtCore.QRect(1, 25, 400, 375))
        self.input_img.setAutoFillBackground(True)
        self.input_img.setScaledContents(True)
        self.input_img.setText("                                 image")
        self.input_img.setObjectName("input_img")
        self.input_img.setFont(font_bl)
        self.input_img.setStyleSheet("color: blue;""background-color: white;" )



        self.out_img = QtWidgets.QLabel(self.out_frame)
        self.out_img.setGeometry(QtCore.QRect(1, 25, 400, 375))
        self.out_img.setAutoFillBackground(True)
        self.out_img.setScaledContents(True)
        self.out_img.setText("                                   image")
        self.out_img.setObjectName("out_img")
        self.out_img.setFont(font_bl)
        self.out_img.setStyleSheet("color: blue;""background-color: white;" )



        self.text_label = QtWidgets.QLabel(self.text_frame)
        self.text_label.setGeometry(QtCore.QRect(270, 40, 480, 170))
        self.text_label.setFont(font_bl)
        self.text_label.setAutoFillBackground(True)
        self.text_label.setTextFormat(QtCore.Qt.PlainText)
        self.text_label.setScaledContents(False)
        self.text_label.setText("")
        self.text_label.setObjectName("text_label")
        self.text_label.setStyleSheet("color: blue;""background-color: white;" )


        self.txt_le = QtWidgets.QLabel(self.text_frame)
        self.txt_le.setGeometry(QtCore.QRect(480, 5, 111, 31))
        self.txt_le.setFont(font_bl)
        self.txt_le.setText("Text")
        self.txt_le.setObjectName("txe_le")
       
        
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 809, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        
        self.menubar.triggered['QAction*'].connect(self.returnPressedSlot)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        ################################# Functions #############################

    def _open_file_dialog(self): # a function to open the dialog window
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        
        result =QFileDialog.getOpenFileName(self, 'Open file', 
         'E:\\',"All Files (*);; Image files (*.jpg *.gif *.jpeg)",'',options)


        
         
        self.textBrowser.setText('{}'.format(result[0]))
        self.input_img.setPixmap(QPixmap(result[0]))
        print(result[0])
        return result[0]

    


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AFTER LIGHT INSIGHT"))
        self.Save_bt.setText(_translate("MainWindow", "Save Hist"))
        self.hist_bt.setText(_translate("MainWindow", "Show Hist"))
        self.Enhance_bt.setText(_translate("MainWindow", "Enhance"))
        self.text_bt.setText(_translate("MainWindow", "get text"))
        self.browse_lable.setText(_translate("MainWindow", "select image :"))
        self.input_label.setText(_translate("MainWindow", "input image"))
        self.browse_bt.setText(_translate("MainWindow", "Browse"))

    def returnPressedSlot( self ):
        pass

    def show_hist (self):

        pass



    def getText (self):

       pass

    def Save( self  ): #  replace it  save hist

        pass
        
    def Enhance( self ):

        pass


        ########## help functions ############

    def new_img_name(self):
        
        pass
    
    def enhance_image(self,path, new_path="", write=0):

        image = cv2.imread(path)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
        hist_size = len(hist)

        # Calculate cumulative distribution from the histogram
        accumulator = []
        accumulator.append(float(hist[0]))
        for index in range(1, hist_size):
            accumulator.append(accumulator[index - 1] + float(hist[index]))

        # Locate points to clip
        maximum = accumulator[-1]
        clip_hist_percent = (maximum / 200.0)
        
        # Locate left cut
        minimum_gray = 0
        while accumulator[minimum_gray] < clip_hist_percent:
            minimum_gray += 1

        # Locate right cut
        maximum_gray = hist_size - 1
        while accumulator[maximum_gray] >= (maximum - clip_hist_percent):
            maximum_gray -= 1

        # Calculate alpha and beta values
        alpha = 255 / (maximum_gray - minimum_gray)
        beta = -minimum_gray * alpha


        enhanced_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
        if write == 1:
            cv2.imwrite(new_path, enhanced_image)
        return enhanced_image
    

    
    if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
