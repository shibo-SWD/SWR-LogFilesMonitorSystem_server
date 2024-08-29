from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QStatusBar, QAction, QMenuBar, QToolBar, QSplitter, QApplication, QDialog, QFormLayout, QSpacerItem, QSizePolicy
)

from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QSize
import subprocess
import sys

from utils.connection_utils import get_local_ip_address

def setup_ui(main_window):
    """初始化主窗口的UI组件和布局"""
    main_window.setWindowTitle('赛威德打磨软件文件监控服务端')
    main_window.setWindowIcon(QIcon('data/doc/SoftwareLogo.png'))
    main_window.resize(1024, 768)

    # 设置初始字体大小
    font = QFont()
    font.setPointSize(12)
    main_window.setFont(font)

    # 创建主分隔器
    main_splitter = QSplitter(Qt.Horizontal)
    main_splitter.setHandleWidth(0)  # 隐藏水平分隔器的拖动边框

    # 图标栏（左侧）
    icon_bar = QToolBar(main_window)
    icon_bar.setOrientation(Qt.Vertical)
    icon_bar.setIconSize(QSize(32, 32))  # 设置图标按钮大小
    icon_bar.setFixedWidth(60)  # 工具栏宽度

    # 添加图标按钮到图标栏
    icon_button1 = QAction(QIcon('./data/images/ConnectIcon.png'), 'Button 1', main_window)
    icon_button1.triggered.connect(lambda: switch_content(main_window, 'content1'))
    icon_bar.addAction(icon_button1)

    # 添加一个空白的分隔符来增加按钮间隔
    icon_bar.addSeparator()

    icon_button2 = QAction(QIcon('./data/images/DataAnalysis.png'), 'Button 2', main_window)
    icon_button2.triggered.connect(lambda: show_path_dialog(main_window))
    icon_bar.addAction(icon_button2)

    # 添加图标栏到主分隔器
    main_splitter.addWidget(icon_bar)

    # 创建右侧的垂直分隔器
    right_splitter = QSplitter(Qt.Vertical)

    # 创建操作空间（上部 80%）
    operation_widget = QWidget()
    main_window.operation_layout = QVBoxLayout()  # 修改：将 operation_layout 赋给 main_window
    operation_widget.setLayout(main_window.operation_layout)

    # 添加均匀间隔的空间项
    spacer1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
    spacer2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
    spacer3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
    main_window.operation_layout.addSpacerItem(spacer1)
    
    # 本地IP地址显示
    main_window.ip_line_edit = QLineEdit(main_window)
    main_window.ip_line_edit.setText(get_local_ip_address())
    main_window.ip_line_edit.setReadOnly(True)
    main_window.operation_layout.addWidget(QLabel('本地 IP 地址:'))
    main_window.operation_layout.addWidget(main_window.ip_line_edit)

    # 日志保存地址输入框
    main_window.save_dir_input = QLineEdit(main_window)
    main_window.save_dir_input.setText('./data/received_files')
    main_window.operation_layout.addWidget(QLabel('监控日志保存地址:'))
    main_window.operation_layout.addWidget(main_window.save_dir_input)

    # 启动和关闭按钮
    main_window.start_button = QPushButton('启动服务器')
    main_window.start_button.clicked.connect(main_window.start_server)
    main_window.operation_layout.addWidget(main_window.start_button)

    main_window.stop_button = QPushButton('关闭服务器')
    main_window.stop_button.setEnabled(False)
    main_window.stop_button.clicked.connect(main_window.stop_server)
    main_window.operation_layout.addWidget(main_window.stop_button)

    # 添加均匀间隔的空间项
    main_window.operation_layout.addSpacerItem(spacer2)
    main_window.operation_layout.addSpacerItem(spacer3)

    # 添加操作空间到右侧分隔器
    right_splitter.addWidget(operation_widget)

    # 日志显示区域（下部 20%）
    log_widget = QWidget()
    log_layout = QVBoxLayout()
    log_widget.setLayout(log_layout)

    main_window.log_text = QTextEdit()
    main_window.log_text.setReadOnly(True)
    log_layout.addWidget(main_window.log_text)

    # 状态显示
    main_window.status_label = QLabel('服务器未启动')
    log_layout.addWidget(main_window.status_label)

    # 添加日志空间到右侧分隔器
    right_splitter.addWidget(log_widget)

    # 设置分隔器的比例（80%操作空间，20%日志空间）
    right_splitter.setStretchFactor(0, 8)
    right_splitter.setStretchFactor(1, 2)

    # 将右侧分隔器添加到主分隔器
    main_splitter.addWidget(right_splitter)

    # 设置中央小部件
    main_window.setCentralWidget(main_splitter)

    # 状态栏
    main_window.status_bar = QStatusBar()
    main_window.setStatusBar(main_window.status_bar)

    # 菜单栏
    setup_menu_bar(main_window)

def switch_content(main_window, content_name):
    """根据所选图标按钮切换显示的内容"""
    # 清空操作空间的内容
    for i in reversed(range(main_window.operation_layout.count())): 
        widget = main_window.operation_layout.itemAt(i).widget()
        if widget:
            widget.deleteLater()

    if content_name == 'content1':
        # 显示与 content1 相关的 UI
        # label = QLabel('Content 1 is displayed')
        # main_window.operation_layout.addWidget(label)
        pass
    elif content_name == 'content2':
        # 显示与 content2 相关的 UI
        # label = QLabel('Content 2 is displayed')
        # main_window.operation_layout.addWidget(label)
        pass

def show_path_dialog(main_window):
    """显示路径输入对话框"""
    dialog = QDialog(main_window)
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