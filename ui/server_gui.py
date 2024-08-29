# server_gui.py

from PyQt5.QtWidgets import (
    QMainWindow
)
from PyQt5.QtGui import QIcon, QFont   # 导入 QIcon 模块

from server.server_control import ServerController
from ui.fonts import FontSizeDialog, FontManager
from ui.communicator import Communicator
from ui.theme_manager import ThemeManager
from ui.layout_manager import setup_ui


class ServerGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.file_server = None
        self.communicator = Communicator()
        self.theme_manager = ThemeManager(self)
        self.font_manager = FontManager(self)
        self.server_controller = ServerController(self.communicator)
        self.current_theme = 'light'  # 初始化为明亮主题

        setup_ui(self)

        # 连接信号与槽
        self.communicator.status_update.connect(self.update_status_label)
        self.communicator.log_update.connect(self.update_log_text)
        self.communicator.server_started.connect(self.on_server_started)
        self.communicator.server_stopped.connect(self.on_server_stopped)

    def start_server(self):
        """启动服务器"""
        save_dir_path = self.save_dir_input.text()
        if not save_dir_path:
            save_dir_path = './data/received_files'
        self.server_controller.start_server(save_dir_path)

    def stop_server(self):
        """关闭服务器"""
        self.server_controller.stop_server()

    def update_status_label(self, status_text):
        """更新状态标签"""
        self.status_label.setText(status_text)

    def update_log_text(self, log_text):
        """更新日志文本区域"""
        self.log_text.append(log_text)

    def on_server_started(self):
        """服务器启动后的处理"""
        self.status_bar.showMessage('服务器已启动')
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.communicator.log_update.emit('服务器已启动...')

    def on_server_stopped(self):
        """服务器停止后的处理"""
        self.status_bar.showMessage('服务器已停止')
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.communicator.log_update.emit('服务器已停止...')

    def show_about(self):
        """显示关于信息"""
        self.log_text.append('关于：这是一个文件监控服务端程序，使用 PyQt5 构建。')

    def open_font_size_dialog(self):
        """打开字体大小调整对话框"""
        font_dialog = FontSizeDialog(self)
        font_dialog.exec_()
        self.font_manager.set_font_size(font_dialog.slider.value())  # 使用 FontManager 设置字体

    def show_path_dialog(self):
        """显示路径输入对话框"""
        dialog = QDialog(self)
        dialog.setWindowTitle('输入路径')
        dialog.setFixedSize(300, 120)

        layout = QFormLayout(dialog)

        path_input = QLineEdit(dialog)
        layout.addRow(QLabel('路径:'), path_input)

        confirm_button = QPushButton('确认', dialog)
        confirm_button.clicked.connect(lambda: run_streamlit(path_input.text(), dialog))
        layout.addWidget(confirm_button)

        dialog.exec_()

    def run_streamlit(path, dialog):
        """在指定路径下运行 streamlit"""
        try:
            subprocess.Popen(['streamlit', 'run', 'main.py'], cwd=path)
        except Exception as e:
            print(f"Error running Streamlit: {e}")
        finally:
            dialog.accept()
