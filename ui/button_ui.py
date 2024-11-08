from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QSpacerItem, QSizePolicy
)

from utils.connection_utils import get_local_ip_address
def clean_operation_ui(main_window):
    # 清空操作空间的内容
    try:
        for i in reversed(range(main_window.operation_layout.count())): 
            widget = main_window.operation_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()
    except RuntimeError as e:
        print(f"RuntimeError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def draw_connect_ui(main_window):

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


