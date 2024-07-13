from openai import OpenAI, APIConnectionError
import urllib.request 
import time
import os





def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon(resource_path("icon.png"))) 
        MainWindow.resize(910, 562)
        MainWindow.setStyleSheet("background-color: rgb(29, 29, 29);\n"
"selection-background-color: rgb(85, 170, 255);\n"
"selection-color: rgb(74, 74, 74);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.heroText = QtWidgets.QLabel(self.centralwidget)
        self.heroText.setGeometry(QtCore.QRect(10, 10, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.heroText.setFont(font)
        self.heroText.setAutoFillBackground(False)
        self.heroText.setStyleSheet("color:rgb(217, 217, 217);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.heroText.setTextFormat(QtCore.Qt.PlainText)
        self.heroText.setAlignment(QtCore.Qt.AlignCenter)
        self.heroText.setObjectName("heroText")
        self.generateButton = QtWidgets.QPushButton(self.centralwidget)
        self.generateButton.setGeometry(QtCore.QRect(20, 350, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)

        # genereate button
        self.generateButton.setFont(font)
        self.generateButton.setStyleSheet("color: white;\n"
"background-color: rgb(0, 85, 0);")
        self.generateButton.setCheckable(False)
        self.generateButton.setDefault(False)
        self.generateButton.setFlat(False)
        self.generateButton.setObjectName("generateButton")

        # image window
        self.imageWindow = QtWidgets.QLabel(self.centralwidget)
        self.imageWindow.setGeometry(QtCore.QRect(370, 20, 512, 512))
        self.imageWindow.setMaximumSize(QtCore.QSize(512, 512))
        self.imageWindow.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(255, 255, 255);")
        self.imageWindow.setText("")
        self.imageWindow.setPixmap(QtGui.QPixmap(resource_path("default.png")))
        self.imageWindow.setScaledContents(True)
        self.imageWindow.setObjectName("imageWindow")

        # api input box
        self.apiField = QtWidgets.QLineEdit(self.centralwidget)
        self.apiField.setGeometry(QtCore.QRect(20, 110, 201, 21))
        self.apiField.setAutoFillBackground(False)
        self.apiField.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.apiField.setObjectName("apiField")
        self.apiField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.promptField = QtWidgets.QLineEdit(self.centralwidget)
        self.promptField.setGeometry(QtCore.QRect(20, 200, 271, 31))
        self.promptField.setAutoFillBackground(False)
        self.promptField.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.promptField.setObjectName("promptField")
        self.getApiLink = QtWidgets.QLabel(self.centralwidget)
        self.getApiLink.setGeometry(QtCore.QRect(240, 110, 55, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        font.setUnderline(True)
        self.getApiLink.setOpenExternalLinks(True)
        self.getApiLink.setFont(font)
        self.getApiLink.setStyleSheet("color:rgb(157, 159, 255)")
        self.getApiLink.setAlignment(QtCore.Qt.AlignCenter)
        self.getApiLink.setObjectName("getApiLink")

   
        # drop down list
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 280, 271, 31))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        
        # progress bar
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(370, 10, 512, 10))
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 910, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AI Image Generator 1.1"))
        self.heroText.setText(_translate("MainWindow", "AI Image Generator"))
        self.generateButton.setText(_translate("MainWindow", "Generate"))
        self.generateButton.clicked.connect(lambda:self.generate())
        self.apiField.setPlaceholderText(_translate("MainWindow", "API Key"))
        self.promptField.setPlaceholderText(_translate("MainWindow", "Enter Prompt"))
        self.getApiLink.setText(_translate("MainWindow", "<a href=https://platform.openai.com/account/api-keys>API</a>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Cartoon"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Impressionism"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Octane Render"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Low Poly"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Watercolour"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Illustrator"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Anime"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Neo Noir"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Ultra Realistic"))

        # shows the popup error message if fields are left blank
    def showPopup(self):
        dialog = QMessageBox(MainWindow)
        dialog.setWindowTitle("Error!")
        dialog.setText("Fields can't be left blank!")
        dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        dialog.exec_()

        # shows api error message if api key is invalid or no credits remaining
    def apiError(self, e):
        apiDialog = QMessageBox(MainWindow)
        apiDialog.setWindowTitle("Error!")
        apiDialog.setText("Invalid API or no credits remaining!")
        apiDialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        print(e)
        apiDialog.exec_()

    # progress bar
    def progBar(self):
        for i in range(0, 101):
             time.sleep(0.01)
             self.progressBar.setProperty("value", i)

    # generate image
    def generate(self):
        api_key = self.apiField.text()
        client = OpenAI(api_key=api_key)
        prompt = self.promptField.text()
        combo_text = self.comboBox.currentText()
        if len(api_key) == 0 or len(prompt) == 0: # check if all fields are filled
                self.showPopup()  
                
        else: 
                self.progBar()
                user_prompt = str(prompt + " in the style of " + combo_text)
                print(user_prompt)
                try:
                        response = client.images.generate(prompt=user_prompt,
                        n=1,
                        size="1024x1024")
                        image_url = response.data[0].url
                        print(image_url)
                        file_name = "image.png"
                        urllib.request.urlretrieve(image_url, file_name)
                        self.imageWindow.setPixmap(QtGui.QPixmap("image.png"))
                except APIConnectionError as e:
                        self.apiError(e)

if __name__ == "__main__":
    import sys
    global client
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())