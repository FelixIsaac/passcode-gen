import sys
import time
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QCheckBox, QPushButton
from app import generate

class Window(QWidget):
  def __init__(self):
    # initialize
    self.width = 300
    self.height = 500
    QWidget.__init__(self)
    # generate password
    self.password = QLineEdit(generate(), parent = self)
    self.password.setEnabled(False)
    self.password.setFixedWidth(310)
    self.password.setStyleSheet("font: 15pt")
    self.password.move(80, 20)
    # Copy password button
    self.copy = QPushButton("Copy", self)
    self.copy.move(200, 50)
    self.copy.clicked.connect(self.copyPassword)
    # Letter checkbox
    self.letters = QCheckBox("Letters", self)
    self.letters.stateChanged.connect(self.changePassword)
    self.letters.move(100, 100)
    self.letters.setChecked(True)
    # Digits checkbox
    self.digits = QCheckBox("Digits", self)
    self.digits.stateChanged.connect(self.changePassword)
    self.digits.move(200, 100)
    self.digits.setChecked(True)
    # Symbols checkbox
    self.symbols = QCheckBox("Symbols", self)
    self.symbols.stateChanged.connect(self.changePassword)
    self.symbols.move(300, 100)
    self.symbols.setChecked(True)
    # Character length
    self.length = QLineEdit("28", parent = self)
    self.length.move(165, 130)
    self.length.textChanged.connect(self.changePassword)
    
  def copyPassword(self, state):
    if state:
      # copy text
      if state != "Password is too weak!": QApplication.clipboard().setText(state)
    else:
      self.copyPassword(self.password.text())
    
  def changePassword(self, state):
    # Check if window object has the follow attrs
    if hasattr(self, 'letters') and hasattr(self, 'digits') and hasattr(self, 'symbols') and hasattr(self, 'length'):
      # check at least one of letters or digits or symbols
      if self.letters.isChecked() or self.digits.isChecked() or self.symbols.isChecked():
        # check if length is not less than 1
        if len(str(self.length.text())):
          password = generate(
            length= int(self.length.text()),
            letters=self.letters.isChecked(),
            digits=self.digits.isChecked(),
            symbols=self.symbols.isChecked()
          )
          
          self.password.setText(password)
          if (password != "Password is too weak!"): self.copyPassword(password)
      else:
        self.symbols.setChecked(True)
        self.changePassword(state)

if __name__ == "__main__":
  # Initialize
  app = QApplication(sys.argv)
  # GUI
  window = Window()
  window.setWindowTitle('Password generator')
  window.setGeometry(0, 0, 470, 165)
  window.show()
  # Main loop
  sys.exit(app.exec_())