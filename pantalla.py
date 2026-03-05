import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit
from PyQt6.QtCore import Qt

class RechnerSchild(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rechner Schild (PyQt6)")
        self.setFixedSize(300, 400)

        layout = QGridLayout()

        self.display = QLineEdit()
        self.display.setFixedHeight(50)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True) # Nur zum Anzeigen
        layout.addWidget(self.display, 0, 0, 1, 4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row, col = 1, 0
        for btn_text in buttons:
            button = QPushButton(btn_text)
            button.setFixedSize(60, 60)
            
            layout.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenster = RechnerSchild()
    fenster.show()
    sys.exit(app.exec())

