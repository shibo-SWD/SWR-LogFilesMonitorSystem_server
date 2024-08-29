# server_gui.py

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, 
    QTextEdit, QStatusBar, QAction, QMenuBar, QLineEdit
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

    # def initUI(self):
    #     """初始化UI组件"""
    #     self.setWindowTitle('赛威德打磨软件文件监控服务端')
    #     self.setWindowIcon(QIcon('data/doc/SoftwareLogo.png'))  # 设置窗口图标
    #     self.resize(600, 400)  # 设置窗口大小

    #     # 设置初始字体大小
    #     font = QFont()
    #     font.setPointSize(12)  # 将字体大小设置为 12，可以根据需要调整大小
    #     self.setFont(font)

    #     # 中央Widget
    #     central_widget = QWidget()
    #     self.setCentralWidget(central_widget)
    #     layout = QVBoxLayout()

    #     # 状态显示
    #     self.status_label = QLabel('服务器未启动')
    #     layout.addWidget(self.status_label)

    #     # 将 QLabel 改为 QLineEdit 显示 IP 地址并设置为只读
    #     self.ip_line_edit = QLineEdit(self)
    #     self.ip_line_edit.setText(get_local_ip_address())
    #     self.ip_line_edit.setReadOnly(True)  # 设置为只读
    #     layout.addWidget(QLabel('本地 IP 地址:'))
    #     layout.addWidget(self.ip_line_edit)

    #     # 日志保存地址输入框
    #     self.save_dir_input = QLineEdit(self)
    #     self.save_dir_input.setText('./data/received_files')
    #     layout.addWidget(QLabel('监控日志保存地址:'))
    #     layout.addWidget(self.save_dir_input)

    #     # 启动和关闭按钮
    #     self.start_button = QPushButton('启动服务器')
    #     self.start_button.clicked.connect(self.start_server)
    #     layout.addWidget(self.start_button)

    #     self.stop_button = QPushButton('关闭服务器')
    #     self.stop_button.setEnabled(False)
    #     self.stop_button.clicked.connect(self.stop_server)
    #     layout.addWidget(self.stop_button)

    #     # 日志显示区域
    #     self.log_text = QTextEdit()
    #     self.log_text.setReadOnly(True)
    #     layout.addWidget(self.log_text)

    #     central_widget.setLayout(layout)

    #     # 状态栏
    #     self.status_bar = QStatusBar()
    #     self.setStatusBar(self.status_bar)

    #     # 菜单栏
    #     menubar = self.menuBar()
    #     file_menu = menubar.addMenu('文件')
    #     about_action = QAction('关于', self)
    #     about_action.triggered.connect(self.show_about)
    #     file_menu.addAction(about_action)

    #     exit_action = QAction('退出', self)
    #     exit_action.triggered.connect(self.close)
    #     file_menu.addAction(exit_action)

    #     # 添加字体调整选项
    #     settings_menu = menubar.addMenu('设置')
    #     font_action = QAction('调整字体大小', self)
    #     font_action.triggered.connect(self.open_font_size_dialog)
    #     settings_menu.addAction(font_action)

    #     # 主题选择菜单
    #     theme_menu = menubar.addMenu('主题')
    #     light_theme_action = QAction('明亮主题', self)
    #     light_theme_action.triggered.connect(self.theme_manager.set_light_theme)
    #     theme_menu.addAction(light_theme_action)

    #     dark_theme_action = QAction('暗黑主题', self)
    #     dark_theme_action.triggered.connect(self.theme_manager.set_dark_theme)
    #     theme_menu.addAction(dark_theme_action)

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


