import  sys
import random
from PyQt5.QtWidgets import QApplication , QMainWindow , QLabel , QWidget , QVBoxLayout, QLineEdit, QRadioButton , QButtonGroup , QPushButton
from PyQt5.QtGui import QFont
from PyQt5 import QtCore



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Random Password Maker")
        self.setGeometry(500 , 300 , 1000 , 1000 )
        # defining label for result 
        self.result_label = QLabel(" " , self)
        
        # defining label for ask about number of characters
        self.character_counter_ask_label = QLabel("How many character? " , self)

        # input for entering the number of character user wants 
        self.input_number_characters = QLineEdit(self)
        
        # defining label for ask about is there must be a number or not
        self.any_number_label = QLabel("Any number? " , self)
        
        # defining yes/no radio button for the any_number_label answer
            # first defining groupe
        self.any_number_answer_group = QButtonGroup(self)
        self.yes_any_number_answer = QRadioButton("Yes" , self)
        self.no_any_number_answer = QRadioButton("No" , self) 
        
        # defining label for number of digits 
        self.digits_counter_label = QLabel("How many digits? " , self)

        # defining input for enter the number of digits
        self.input_digits_counter = QLineEdit(self)
        
        # defining label for ask about how many upper case letter must be?
        self.upper_case_counter_label = QLabel("How many UPPER CASE? " , self)
        
        # defining input for upper_case_counter_label
        self.input_upper_case_counter = QLineEdit(self)
        
        # defining label for ask about is there any special character?
        self.is_any_special_character_label = QLabel("Any special character?(! , @ , ...) " , self)
         
        # defining yes/no radio button for the any_special_character answer
            # first defining groupe
        self.any_special_character_group = QButtonGroup(self)
        self.yes_special_character = QRadioButton("Yes" , self)
        self.no_special_character = QRadioButton("No" , self) 

        # defining label for asking about the number of special characters
        self.speical_character_counter_label = QLabel("How many special Charater? " , self)
        
        # defining input for special_character_counter 
        self.input_special_character_counter = QLineEdit(self)
        
        # difining button for the result
        self.make_pass_button = QPushButton("Make me a password" , self)
        
        self.any_number_clicked = None
        self.any_special_clicked = None

        self.initUI()







    def initUI(self):
        
        # work with result label
        self.result_label.setGeometry(50 , 20 , 900 , 100)
        self.result_label.setStyleSheet(
            "background-color: #5a5a5c;"
        )
        self.result_label.setAlignment(QtCore.Qt.AlignCenter)
        
        # work with character counter label
        self.character_counter_ask_label.setGeometry(150 , 170 , 400 , 50)
        self.character_counter_ask_label.setStyleSheet(
            "background-color: #ffffff;"
            "font-family:ComicShannsMono Nerd Font;"
            "font-size: 20px"
        )
        self.character_counter_ask_label.setAlignment(QtCore.Qt.AlignCenter)
        
        # work with input number character
        self.input_number_characters.setStyleSheet(
            "background-color: #ffffff;"
            "font-family:ComicShannsMono Nerd Font;"
            "font-size: 20px"
        )
        self.input_number_characters.setGeometry(600 , 170 , 100 , 50) 
        
        # work with any number label
        self.any_number_label.setGeometry(150 , 250 , 400 , 50) 
        self.any_number_label.setStyleSheet(
            "background-color: #ffffff;"
            "font-family:ComicShannsMono Nerd Font;"
            "font-size: 20px"
        )
        self.any_number_label.setAlignment(QtCore.Qt.AlignCenter)
        
        # work with any_number_label radio button
        self.any_number_answer_group.addButton(self.yes_any_number_answer)
        self.any_number_answer_group.addButton(self.no_any_number_answer)
        self.yes_any_number_answer.setGeometry(600 , 270 , 50 , 20)
        self.yes_any_number_answer.setStyleSheet(
            "font-family:ComicShannsMono Nerd Font;"
            "font-size: 17px"
        )
        self.yes_any_number_answer.toggled.connect(self.yes_any_number_button_clicked)
        self.no_any_number_answer.setGeometry(670 , 270 , 50 , 20)
        self.no_any_number_answer.setStyleSheet(
            "font-family:ComicShannsMono Nerd Font;"
            "font-size: 17px"
        ) 
        self.no_any_number_answer.toggled.connect(self.no_any_number_button_clicked)

        # work with digits counter label
        self.digits_counter_label.setGeometry(150 , 330 , 400 , 50)
        self.digits_counter_label.setStyleSheet(
            "background-color: #ffffff;"
            "font-family:ComicShannsMono Nerd Font;"
            "font-size: 20px;"
            "color:#c8c8cc"
        )
        self.digits_counter_label.setAlignment(QtCore.Qt.AlignCenter)
        
         # work with input digits counter label
        self.input_digits_counter.setGeometry(600 , 330 , 100 , 50)
        self.input_digits_counter.setStyleSheet(
            "font-family:ComicShannsMono Nerd Font;"
            "font-size: 20px;"
        )
        self.input_digits_counter.setDisabled(True)
        
        # work with upper_case_counter label
        self.upper_case_counter_label.setGeometry(150 , 400 , 400 , 50)
        self.upper_case_counter_label.setStyleSheet(
            "background-color: #ffffff;"
            "font-family:ComicShannsMono Nerd Font;"
            "font-size: 20px;"
        )
        self.upper_case_counter_label.setAlignment(QtCore.Qt.AlignCenter)
        
        # work input for upper_case_counter
        self.input_upper_case_counter.setGeometry(600, 400 ,100 , 50) 
        
        self.input_upper_case_counter.setStyleSheet(
            "background-color: #ffffff;"
            "font-family:ComicShannsMono Nerd Font;"
            "font-size: 20px"
        )
        
        # work any_special_character label
        self.is_any_special_character_label.setGeometry(150 , 480 , 400 , 50) 
        self.is_any_special_character_label.setStyleSheet(
            "background-color: #ffffff;"
            "font-family:ComicShannsMono Nerd Font;"
            "font-size: 20px;"
        )
        self.is_any_special_character_label.setAlignment(QtCore.Qt.AlignCenter)
        
        # work yes/no radio buttons for special character
         
        self.any_special_character_group.addButton(self.yes_special_character)
        self.any_special_character_group.addButton(self.no_special_character)
        self.yes_special_character.setGeometry(600 , 500 , 50 , 20)
        self.yes_special_character.setStyleSheet(
            "font-family:ComicShannsMono Nerd Font;"
            "font-size: 17px"
        )
        
        self.yes_special_character.toggled.connect(self.yes_special_character_clicked)
        
        self.no_special_character.toggled.connect(self.no_special_character_clicked)
        self.no_special_character.setGeometry(670 , 500 , 50 , 20)
        self.no_special_character.setStyleSheet(
            "font-family:ComicShannsMono Nerd Font;"
            "font-size: 17px"
        ) 
        
        
        # work special_character_counter label
        self.speical_character_counter_label.setGeometry(150 , 550 , 400 , 50)
        self.speical_character_counter_label.setAlignment(QtCore.Qt.AlignCenter)
        self.speical_character_counter_label.setStyleSheet(
            "background-color: #ffffff;"
            "font-family:ComicShannsMono Nerd Font;"
            "font-size: 20px;"
            "color:#c8c8cc"
        )
        
        
        # work input special_character_counter
        self.input_special_character_counter.setGeometry(600 , 550 , 100 , 50)
        self.input_special_character_counter.setStyleSheet(
            "font-family:ComicShannsMono Nerd Font;"
            "font-size: 20px;"
        )
        self.input_special_character_counter.setDisabled(True)
        
        # work with make me a password button
        self.make_pass_button.setGeometry(350 , 650 , 250 , 50)
        self.make_pass_button.setObjectName("btn")
        self.setStyleSheet("""
                           QPushButton#btn{
                                border-radius: 15px;
                                border: 3px solid;
                                background-color: #089c20;
                            }
                            QPushButton#btn:hover{ 
                                background-color: #10eb35;
                            }
                            """
        )
        self.make_pass_button.clicked.connect(self.make_pass_on_clicked)
        


        







    def yes_any_number_button_clicked(self): 
        self.any_number_clicked = 1
        yes_any_number_button = self.sender()
        if yes_any_number_button.isChecked():
            self.digits_counter_label.setStyleSheet(
                "background-color: #ffffff;"
                "font-family:ComicShannsMono Nerd Font;"
                "font-size: 20px;"
                "color: black"
            )
            self.input_digits_counter.setDisabled(False)
        else:
            self.digits_counter_label.setStyleSheet(
                "background-color: #ffffff;"
                "font-family:ComicShannsMono Nerd Font;"
                "font-size: 20px;"
                "color:#c8c8cc"
            )
            self.input_digits_counter.setText(" ")
            self.result_label.setText(" ")
            self.input_digits_counter.setDisabled(True)

            
            
    def no_any_number_button_clicked(self):
        self.any_number_clicked = 0          
            
            
            
            
    def yes_special_character_clicked(self): 
        self.any_special_clicked = 1
        yes_any_number_button_clicked = self.sender()
        if yes_any_number_button_clicked.isChecked():
            self.speical_character_counter_label.setStyleSheet(
                "background-color: #ffffff;"
                "font-family:ComicShannsMono Nerd Font;"
                "font-size: 20px;"
            )
            self.input_special_character_counter.setDisabled(False)
        else:
            self.speical_character_counter_label.setStyleSheet(
                "background-color: #ffffff;"
                "font-family:ComicShannsMono Nerd Font;"
                "font-size: 20px;"
                "color:#c8c8cc"
            )
            self.input_special_character_counter.setText(" ")
            self.input_special_character_counter.setDisabled(True)
    def no_special_character_clicked(self):
        self.any_special_clicked = 0
         
    def make_pass_on_clicked(self):
        error = None
        result = None
        error_counter= 0
       
        try:
            if (self.input_number_characters.text()):
                character_number = int(self.input_number_characters.text())
                if(6 <= character_number <= 12):
                    digit_number = None
                    upper_case_number = None
                    special_number = None
                    if(self.any_number_clicked == 1):
                        if(not self.input_digits_counter.text()):
                            error = "You need to enter the number of digit!"
                            error_counter += 1
                            self.result_label.setText(error)
                        else:
                            error_counter = 0
                    elif(self.any_number_clicked == 0):
                        error_counter = 0
                    else:
                        error_counter += 1
                        error = "You need to choose you want to have number in your password or not!" 
                    if(error_counter == 0):
                        if(self.any_special_clicked == 1):
                            if(not self.input_special_character_counter.text()):
                                error = ""
                        elif(self.any_special_clicked == 0):
                            
                        else:
                    else:
                        
                        
        except:
            self.result_label.setText("invalid type!")

            
            
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())



if __name__ == "__main__":
    main()