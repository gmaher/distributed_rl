from multiprocessing import Process
from Queue import Queue
import socket
import threading

class AbstractCore(object):
    def __init__(self):

    def handle_message(self,header,data):
        pass

class message_bus(threading.Thread):
    def __init__(self,address, port, timeout=1, group=None, target=None,
        name="message_bus"):
        self.address = address
        self.port    = port
        self.core    = core
        self.target_address = target_address
        self.target_host    = target_host

        self.msg_q          = Queue(maxsize=queue_size)

        self.socket  = socket.socket(socket.AF_INET,
            socket.SOCK_DGRAM)

        self.socket.bind((self.address, self.port))


class System(Process):
    def __init__(self,address,port,core, target_address, target_host
        queue_size=200, buffer_size=4096):

    def run(self):
