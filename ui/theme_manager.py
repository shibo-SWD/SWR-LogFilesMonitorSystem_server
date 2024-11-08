# theme_manager.py

class ThemeManager:
    def __init__(self, gui):
        self.gui = gui  # 将 ServerGUI 实例保存到 ThemeManager 的一个属性

    def set_theme(self, theme):
        """设置主题，根据主题名称应用样式"""
        if theme not in THEME_STYLES:
            return  # 如果主题不存在，不做任何操作

        # 更新当前主题
        self.gui.current_theme = theme
        self.gui.setStyleSheet(THEME_STYLES[theme]["stylesheet"])
        self.gui.status_bar.showMessage(THEME_STYLES[theme]["status_message"])

    def set_light_theme(self):
        """设置明亮主题"""
        self.set_theme('light')

    def set_dark_theme(self):
        """设置暗黑主题"""
        self.set_theme('dark')


THEME_STYLES = {
    "light": {
        "stylesheet": """
            QMainWindow {
                background-color: white;
                color: black;
            }
            QLabel, QTextEdit, QPushButton {
                background-color: white;
                color: black;
            }
        """,
        "status_message": '已切换到明亮主题'
    },
    "dark": {
        "stylesheet": """
            QMainWindow {
                background-color: #2e2e2e;
                color: white;  /* 保持标题文字为白色，确保在暗黑背景下可见 */
            }
            QLabel, QTextEdit, QPushButton, QLineEdit {
                background-color: #2e2e2e;
                color: white;
                border: 1px solid #444;
            }
            QMenuBar {
                background-color: #2e2e2e;
                color: white;
            }
            QMenuBar::item {
                background-color: #2e2e2e;
                color: white;
            }
            QMenuBar::item:selected {
                background-color: #444;
            }
            QMenu {
                background-color: #2e2e2e;
                color: white;
            }
            QMenu::item:selected {
                background-color: #444;
            }
            QDialog {
                background-color: #2e2e2e;
                color: white;
            }
            QDialog QLabel, QDialog QPushButton, QDialog QLineEdit {
                background-color: #2e2e2e;
                color: white;
                border: 1px solid #444;
            }
            /* 窗口标题字体和颜色设置 */
            QMainWindow::title {
                font-size: 14pt;
                color: white;  /* 确保在深色模式下标题文字是白色的 */
            }
        """,
        "status_message": '已切换到暗黑主题'
    }
}