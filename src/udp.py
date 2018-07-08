import socket

class Threaded(threading.Thread):
    def __init__(self, storage, timeout=3, group=None, target=None, name="threaded",
                 args=(), kwargs=None, verbose=None):
        super(Threaded,self).__init__()
        self.target    = target
        self.name      = name
        self.storage   = storage
        self.timeout   = timeout

    def run(self):
        while True:
            self.execute()
            time.sleep(self.timeout)
        return

    def execute(self):
        raise RuntimeError("Abstract not implemented")

class UDPReceiver(Threaded):
    def setup(self, address, port, buffer_size=1024, storage_key='received'):
        self.host        = address
        self.port        = port
        self.storage_key = storage_key
        self.buffer_size = buffer_size
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.socket.bind((self.host,self.port))

    def execute(self):
        d = self.socket.recvfrom(self.buffer_size)
        data = d[0]
        addr = d[1]
        if not data: return

        self.storage.store(data,self.storage_key)

class UDPBroadcaster(Threaded):
    def setup(self, address, port, buffer_size=1024, storage_key='received'):
        self.host        = address
        self.port        = port
        self.storage_key = storage_key
        self.buffer_size = buffer_size
        self.peers       = []
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.socket.bind((self.host,self.port))

    def addPeer(self, peer):
        self.peers.append(peer)

    def execute(self):
        self.msg = self.storage.get(self.storage_key)
        if not self.msg == None:
            m = self.msg.encode()
            for p in self.peers:
                self.socket.sendto(m,p)
