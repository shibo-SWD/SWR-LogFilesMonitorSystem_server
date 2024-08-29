from PyQt5.QtCore import QObject, pyqtSignal

class Communicator(QObject):
    # 定义信号
    status_update = pyqtSignal(str)
    log_update = pyqtSignal(str)
    server_started = pyqtSignal()
    server_stopped = pyqtSignal()