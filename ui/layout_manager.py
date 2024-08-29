# layout_manager.py

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QStatusBar, QAction, QMenuBar
)
from PyQt5.QtGui import QIcon, QFont

from utils.connection_utils import get_local_ip_address

def setup_ui(main_window):
    """初始化主窗口的UI组件和布局"""
    main_window.setWindowTitle('赛威德打磨软件文件监控服务端')
    main_window.setWindowIcon(QIcon('data/doc/SoftwareLogo.png'))
    main_window.resize(600, 400)

    # 设置初始字体大小
    font = QFont()
    font.setPointSize(12)
    main_window.setFont(font)

    # 中央Widget
    central_widget = QWidget()
    main_window.setCentralWidget(central_widget)
    layout = QVBoxLayout()

    # 本地IP地址显示
    main_window.ip_line_edit = QLineEdit(main_window)
    main_window.ip_line_edit.setText(get_local_ip_address())
    main_window.ip_line_edit.setReadOnly(True)
    layout.addWidget(QLabel('本地 IP 地址:'))
    layout.addWidget(main_window.ip_line_edit)

    # 日志保存地址输入框
    main_window.save_dir_input = QLineEdit(main_window)
    main_window.save_dir_input.setText('./data/received_files')
    layout.addWidget(QLabel('监控日志保存地址:'))
    layout.addWidget(main_window.save_dir_input)

    # 启动和关闭按钮
    main_window.start_button = QPushButton('启动服务器')
    main_window.start_button.clicked.connect(main_window.start_server)
    layout.addWidget(main_window.start_button)

    main_window.stop_button = QPushButton('关闭服务器')
    main_window.stop_button.setEnabled(False)
    main_window.stop_button.clicked.connect(main_window.stop_server)
    layout.addWidget(main_window.stop_button)

    # 日志显示区域
    main_window.log_text = QTextEdit()
    main_window.log_text.setReadOnly(True)
    layout.addWidget(main_window.log_text)

    central_widget.setLayout(layout)

    # 状态显示
    main_window.status_label = QLabel('服务器未启动')
    layout.addWidget(main_window.status_label)

    # 状态栏
    main_window.status_bar = QStatusBar()
    main_window.setStatusBar(main_window.status_bar)

    # 菜单栏
    setup_menu_bar(main_window)

def setup_menu_bar(main_window):
    """初始化菜单栏及其选项"""
    menubar = main_window.menuBar()
    file_menu = menubar.addMenu('文件')

    about_action = QAction('关于', main_window)
    about_action.triggered.connect(main_window.show_about)
    file_menu.addAction(about_action)

    exit_action = QAction('退出', main_window)
    exit_action.triggered.connect(main_window.close)
    file_menu.addAction(exit_action)

    # 添加字体调整选项
    settings_menu = menubar.addMenu('设置')
    font_action = QAction('调整字体大小', main_window)
    font_action.triggered.connect(main_window.open_font_size_dialog)
    settings_menu.addAction(font_action)

    # 主题选择菜单
    theme_menu = menubar.addMenu('主题')
    light_theme_action = QAction('明亮主题', main_window)
    light_theme_action.triggered.connect(main_window.theme_manager.set_light_theme)
    theme_menu.addAction(light_theme_action)

    dark_theme_action = QAction('暗黑主题', main_window)
    dark_theme_action.triggered.connect(main_window.theme_manager.set_dark_theme)
    theme_menu.addAction(dark_theme_action)
