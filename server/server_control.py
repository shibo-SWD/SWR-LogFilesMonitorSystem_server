import threading
from server.server_backend import FileServer

class ServerController:
    def __init__(self, communicator):
        self.file_server = None
        self.communicator = communicator

    def start_server(self, save_dir_path='./data/received_files'):
        """启动服务器"""
        self.file_server = FileServer(save_dir=save_dir_path, log_signal=self.communicator.log_update)
        threading.Thread(target=self._start_server_in_thread, daemon=True).start()

    def _start_server_in_thread(self):
        """后台线程中启动服务器"""
        if self.file_server:
            self.file_server.start()
            # 通过信号更新 GUI
            self.communicator.status_update.emit(f'服务器正在监听 IP: {self.file_server.host} 端口: {self.file_server.port}')
            self.communicator.server_started.emit()

    def stop_server(self):
        """关闭服务器"""
        if self.file_server:
            self.file_server.stop()
            self.communicator.status_update.emit('服务器已停止')
            self.communicator.server_stopped.emit()
