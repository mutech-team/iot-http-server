import socket as s


class Socket:
    socket = None

    def __init__(self, host: str = "mutech.ivica.codes", port: int = 5056):
        self.host = host
        self.port = port
        self.socket = s.socket(s.AF_INET, s.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def send(self, message: str) -> None:
        self.socket.send(message.encode("utf-8"))

    def send(self,topic: str,payload: str):
        
        pass
