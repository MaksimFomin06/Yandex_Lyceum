from PyQt6.QtWidgets import QWidget, QVBoxLayout, QApplication, QPushButton, QLabel, QRadioButton, QGridLayout
import sys


class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Крестики-Нолики')
        self.setGeometry(100, 100, 300, 200)
        self.button_grid = []
        self.init_ui()

    def init_ui(self):
        grid_layout = QGridLayout()
        for i in range(3):
            row = []
            for j in range(3):
                button = QPushButton('', self)
                button.setFixedSize(50, 50)
                button.clicked.connect(lambda _, i=i, j=j: self.make_move(i, j))
                row.append(button)
                grid_layout.addWidget(button, i, j)
            self.button_grid.append(row)

        self.result = QLabel("", self)
        self.x_radio = QRadioButton("X (Первый игрок)", self)
        self.o_radio = QRadioButton("O (Первый игрок)", self)
        self.x_radio.setChecked(True)
        self.x_radio.toggled.connect(self.on_player_choice)
        self.o_radio.toggled.connect(self.on_player_choice)
        self.new_game_button = QPushButton("Новая игра", self)
        self.new_game_button.clicked.connect(self.start_new_game)

        vbox = QVBoxLayout()
        vbox.addLayout(grid_layout)
        vbox.addWidget(self.result)
        vbox.addWidget(self.x_radio)
        vbox.addWidget(self.o_radio)
        vbox.addWidget(self.new_game_button)
        self.setLayout(vbox)

        self.current_player = 'X'
        self.game_active = True
        self.moves_count = 0

    def make_move(self, i, j):
        if not self.game_active or self.button_grid[i][j].text():
            return

        self.button_grid[i][j].setText(self.current_player)
        self.check_winner()
        self.switch_player()

        if not self.game_active:
            self.button_grid[i][j].setEnabled(False)

    def check_winner(self):
        for i in range(3):
            if all(self.button_grid[i][j].text() == self.current_player for j in range(3)):
                self.end_game(f"Выиграл {self.current_player}!")
                return
        for j in range(3):
            if all(self.button_grid[i][j].text() == self.current_player for i in range(3)):
                self.end_game(f"Выиграл {self.current_player}!")
                return
        if all(self.button_grid[i][i].text() == self.current_player for i in range(
            3)) or all(self.button_grid[i][
                2 - i].text() == self.current_player for i in range(3)):
            self.end_game(f"Выиграл {self.current_player}!")
            return
        if self.moves_count >= 9:
            self.end_game("Ничья!")

    def end_game(self, message):
        self.result_label.setText(message)
        self.game_active = False
    
        for row in self.button_grid:
            for button in row:
                button.setEnabled(False)

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        self.moves_count += 1

    def on_player_choice(self):
        if self.x_radio.isChecked():
            self.current_player = 'X'
        elif self.o_radio.isChecked():
            self.current_player = 'O'
        self.start_new_game()

    def start_new_game(self):
        self.game_active = True
        self.moves_count = 0
        self.result.clear()
        for row in self.button_grid:
            for button in row:
                button.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = TicTacToe()
    game.show()
    sys.exit(app.exec())