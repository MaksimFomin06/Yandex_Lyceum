import random
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLCDNumber,
    QSpinBox,
    QPushButton,
    QListWidget,
    QLineEdit,
)


class Pseudonym(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(350, 350)
        self.setWindowTitle("Игра 'Псевдоним'")

        main_layout = QVBoxLayout()
        top_layout = QHBoxLayout()
        bottom_layout = QHBoxLayout()

        self.remainLcd = QLCDNumber()
        self.stones = QSpinBox()
        self.startButton = QPushButton("Начать новую игру")

        top_layout.addWidget(QLabel("Количество камней:"))
        top_layout.addWidget(self.stones)
        top_layout.addWidget(self.startButton)
        top_layout.addStretch()
        top_layout.addWidget(self.remainLcd)

        self.takeInput = QLineEdit()
        self.takeButton = QPushButton("Взять камни")
        self.list_widget = QListWidget()
        self.resultLabel = QLabel("")

        bottom_layout.addWidget(self.takeInput)
        bottom_layout.addWidget(self.takeButton)
        bottom_layout.addStretch()
        bottom_layout.addWidget(self.list_widget)

        main_layout.addLayout(top_layout)
        main_layout.addLayout(bottom_layout)
        main_layout.addWidget(self.resultLabel)

        self.setLayout(main_layout)

        self.stones.setRange(7, 100)
        self.stones.setValue(15)
        self.remainLcd.display(self.stones.value())

        self.startButton.clicked.connect(self.start_game)
        self.takeButton.clicked.connect(self.take_stones)

        self.show()

    def start_game(self):
        num_stones = self.stones.value()
        self.remainLcd.display(num_stones)
        self.list_widget.clear()
        self.resultLabel.setText("")
        self.takeInput.setEnabled(True)
        self.takeButton.setEnabled(True)

    def take_stones(self):
        try:
            taken = int(self.takeInput.text())
            if taken > 0 and taken <= 3:
                remaining = self.remainLcd.intValue() - taken
                self.remainLcd.display(remaining)
                self.list_widget.addItem(f"Пользователь взял {taken} камня.")

                if remaining == 0:
                    self.game_over("Пользователь")
                elif remaining <= 3:
                    self.computer_turn(remaining)
                else:
                    self.takeInput.clear()
                    self.takeInput.setFocus()
            else:
                self.takeInput.clear()
                self.takeInput.setPlaceholderText("Укажите число от 1 до 3!")
        except ValueError:
            self.takeInput.clear()
            self.takeInput.setPlaceholderText("Введите целое число!")

    def computer_turn(self, remaining):
        taken = random.randint(1, min(3, remaining))
        remaining -= taken
        self.remainLcd.display(remaining)
        self.list_widget.addItem(f"Компьютер взял {taken} камня.")

        if remaining == 0:
            self.game_over("Компьютер")

    def game_over(self, winner):
        self.takeInput.setEnabled(False)
        self.takeButton.setEnabled(False)
        self.resultLabel.setText(f"Победа {winner}!")


if __name__ == "__main__":
    app = QApplication([])
    pseudonym = Pseudonym()
    app.exec()