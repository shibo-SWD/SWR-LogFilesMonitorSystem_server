from PyQt5.QtWidgets import (
    QApplication, QVBoxLayout, QLabel, QDialog, QSlider
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class FontSizeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("调整字体大小")
        self.setGeometry(100, 100, 300, 100)
        
        layout = QVBoxLayout()

        # 添加滑块
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(16)
        self.slider.setMaximum(32)
        self.slider.setValue(18)  # 默认字体大小
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(2)
        self.slider.valueChanged.connect(self.update_font_size)

        layout.addWidget(QLabel("选择字体大小:"))
        layout.addWidget(self.slider)

        self.setLayout(layout)

    def update_font_size(self):
        """更新主窗口的字体大小"""
        font_size = self.slider.value()
        self.parent().font_manager.set_font_size(font_size)


class FontManager:
    def __init__(self, gui):
        self.gui = gui  # 保存 GUI 引用
        self.default_font_size = 12  # 默认字体大小
        self.font_size = self.default_font_size

    def set_font_size(self, size):
        """设置整个应用的字体大小"""
        self.font_size = size
        font = QFont()
        font.setPointSize(size)
        self.gui.setFont(font)
        self.apply_theme_specific_styles(size)

    def reset_font_size(self):
        """重置字体大小到默认值"""
        self.set_font_size(self.default_font_size)

    def apply_theme_specific_styles(self, size):
        """根据当前主题应用字体大小和样式"""
        if self.gui.current_theme == 'dark':
            self.gui.setStyleSheet(f"""
                QMainWindow {{
                    background-color: #2e2e2e;
                    color: white;
                }}
                QLabel, QTextEdit, QPushButton, QLineEdit {{
                    background-color: #2e2e2e;
                    color: white;
                    border: 1px solid #444;
                }}
                QMenuBar {{
                    background-color: #2e2e2e;
                    color: white;
                }}
                QMenuBar::item {{
                    background-color: #2e2e2e;
                    color: white;
                }}
                QMenuBar::item:selected {{
                    background-color: #444;
                }}
                QMenu {{
                    background-color: #2e2e2e;
                    color: white;
                }}
                QMenu::item:selected {{
                    background-color: #444;
                }}
                QDialog {{
                    background-color: #2e2e2e;
                    color: white;
                }}
                QDialog QLabel, QDialog QPushButton, QDialog QLineEdit {{
                    background-color: #2e2e2e;
                    color: white;
                    border: 1px solid #444;
                }}
                * {{
                    font-size: {size}px;
                }}
            """)
        else:
            self.gui.setStyleSheet(f"""
                QMainWindow {{
                    background-color: white;
                    color: black;
                }}
                QLabel, QTextEdit, QPushButton {{
                    background-color: white;
                    color: black;
                }}
                * {{
                    font-size: {size}px;
                }}
            """)