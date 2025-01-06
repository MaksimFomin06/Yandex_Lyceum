import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, 
                             QDoubleSpinBox, QPlainTextEdit, QPushButton)


class AntiPlagiarism(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Антиплагиат')
        self.setFixedSize(800, 600)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        self.alert_value = QDoubleSpinBox()
        self.alert_value.setDecimals(2)
        self.alert_value.setSingleStep(0.05)
        self.alert_value.setMinimum(0.00)
        self.alert_value.setMaximum(99.95)
        self.alert_value.setValue(10.00)
        self.alert_value.setSuffix('%')
        label_alert_value = QLabel('Порог срабатывания антиплагиата:')
        self.text1 = QPlainTextEdit()
        self.text1.setPlaceholderText('Вставьте первый текст сюда...')
        self.text2 = QPlainTextEdit()
        self.text2.setPlaceholderText('Вставьте второй текст сюда...')
        self.checkBtn = QPushButton('Проверить на плагиат')
        self.checkBtn.clicked.connect(self.compare_texts)
        layout.addWidget(label_alert_value)
        layout.addWidget(self.alert_value)
        layout.addSpacing(20)
        layout.addWidget(self.text1)
        layout.addWidget(self.text2)
        layout.addSpacing(20)
        layout.addWidget(self.checkBtn)
        self.statusbar = self.statusBar()

    def compare_texts(self):
        threshold = self.alert_value.value()
        text1_lines = set(self.text1.toPlainText().splitlines())
        text2_lines = set(self.text2.toPlainText().splitlines())
    
        if not text1_lines and not text2_lines:
            similarity = 100.0
        elif not text1_lines or not text2_lines:
            similarity = 0.0
        else:
            common_lines = text1_lines & text2_lines
            total_unique_lines = len(text1_lines | text2_lines)
            similarity = round((len(common_lines) / total_unique_lines) * 100, 2)
    
        message = f'Тексты похожи на {similarity:.2f}%'
        if similarity >= threshold:
            message += ', плагиат'
        else:
            message += ', не плагиат'
        self.statusbar.showMessage(message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AntiPlagiarism()
    window.show()
    app.exec()