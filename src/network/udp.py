import socket
from queue import Queue

class Threaded(threading.Thread):
    def __init__(self, sleep_time, group=None, target=None, name="threaded",
                 args=(), kwargs=None, verbose=None):
        super(Threaded,self).__init__()
        self.target       = target
        self.name         = name
        self.sleep_time   = sleep_time

    def run(self):
        while True:
            self.execute()
            time.sleep(self.timeout)
        return

    def execute(self):
        raise RuntimeError("Abstract not implemented")

class UDP(Threaded):
    def setup(self, address, port, serializer, buffer_size=1024, queue_size=200):
        self.address     = address
        self.port        = port
        self.serializer  = serializer
        self.buffer_size = buffer_size
        self.peers       = []

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.socket.bind((self.host,self.port))

        self.received_messages = Queue(maxsize=queue_size)
        self.outgoing_mesasges = Queue(maxsize=queue_size)

    def add_peer(self,peer):
        self.peers.append(peer)

    def execute(self):
        d = self.socket.recvfrom(self.buffer_size)
        data = d[0]
        addr = d[1]
        if not (data == None):
            msg = self.serializer.deserialize(data)
            self.received_messages.put(msg)

        if not self.outgoing_mesasges.empty():
            o_msg = self.outgoing_mesasges.get()
            o_msg = self.serializer.serialize(o_msg)
            o_msg = o_msg.encode()

            for p in self.peers:
                self.socket.sendto(m,p)

    def get_message(self):
        if self.received_messages.empty(): return None
        return self.received_messages.get()

    def send_message(self, data, topic):
        
