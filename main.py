from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QPushButton
import sys
import HANGMAN
from game import get_word, display_word, check_letter

guesses = []
tries = 7

class App(QtWidgets.QMainWindow, HANGMAN.Ui_Dialog):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.setupUi(self)

def guess(form, word):
    global guesses
    global tries
    letter = form.lineEdit.text()
    form.lineEdit.setText("")
    (guesses, found) = check_letter(word, letter, guesses)
    form.label.setText(display_word(word, guesses))
    if found:
        if len(word) == len(guesses):
            form.pushButton_2.setEnabled(False)
            form.label.setText(word)
            popup(form, "You won!")
        else:
            form.label_3.setText("You are right. Guess another letter")
    else:
        tries = tries -1
        draw_img(form,tries)
        form.label_3.setText("Sorry, but wrong :( try another letter. you have " + str(tries) + " tries left")
        if tries == 0:
            form.pushButton_2.setEnabled(False)
            form.label.setText(word)
            popup(form, "Game over")


def draw_img(form, tries):
    if tries == 6:
        form.img.setPixmap(QtGui.QPixmap("assets/hangman/1.png"))
    elif tries == 5:
        form.img.setPixmap(QtGui.QPixmap("assets/hangman/2.png"))
    elif tries == 4:
        form.img.setPixmap(QtGui.QPixmap("assets/hangman/3.png"))
    elif tries == 3:
        form.img.setPixmap(QtGui.QPixmap("assets/hangman/4.png"))
    elif tries == 2:
        form.img.setPixmap(QtGui.QPixmap("assets/hangman/5.png"))
    elif tries == 1:
        form.img.setPixmap(QtGui.QPixmap("assets/hangman/6.png"))
    elif tries == 0:
        form.img.setPixmap(QtGui.QPixmap("assets/hangman/7.png"))

def retry(form,dlg):
    form.pushButton_2.clicked.disconnect()
    start_game(form)
    dlg.close()

def exit():
    sys.exit()

def start_game(form):
    global guesses
    global tries
    guesses = []
    tries = 7
    form.img.setPixmap(QtGui.QPixmap("assets/hangman/0.png"))
    form.label_3.setText("Guess a letter")
    word = get_word()
    form.label.setText(display_word(word, guesses))
    form.pushButton_2.clicked.connect(lambda: guess(form, word))
    form.pushButton_2.setEnabled(True)


def popup(self, text):
    dlg = QDialog(self)
    dlg.setFixedSize(300, 100)
    dlg.setWindowTitle("Hangman")
    txt = QLabel(text, dlg)
    txt.move(70,10)
    font = QtGui.QFont()
    font.setPointSize(30)
    txt.setFont(font)
    txt.setAlignment(QtCore.Qt.AlignCenter)
    retry_btn = QPushButton(dlg)
    retry_btn.setText("Retry")
    retry_btn.move(80,50)
    retry_btn.clicked.connect(lambda:retry(self, dlg))

    exit_btn = QPushButton(dlg)
    exit_btn.setText("Exit")
    exit_btn.move(150,50)
    exit_btn.clicked.connect(exit)
    dlg.exec()


def main():
    app = QApplication(sys.argv)
    form = App()
    form.show()
    start_game(form)
    app.exec_()

if __name__ == '__main__':
    main()
