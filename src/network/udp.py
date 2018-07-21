import socket
from queue import Queue
import threading
import time

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
            time.sleep(self.sleep_time)
        return

    def execute(self):
        raise RuntimeError("Abstract not implemented")

class UDP(Threaded):
    def setup(self, address, port, serializer, timeout=0.5, buffer_size=1024, queue_size=200):
        self.address     = address
        self.port        = port
        self.serializer  = serializer
        self.buffer_size = buffer_size
        self.peers       = {}
        self.timeout     = timeout
        self.queue_size  = queue_size

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.settimeout(self.timeout)

        self.socket.bind((self.address,self.port))

        self.received_messages = {}
        self.outgoing_messages = Queue(maxsize=queue_size)

    def add_peer(self,peer, topic=""):
        if not topic in self.peers:
            self.peers[topic] = []

        self.peers[topic].append(peer)

    def subscribe(self,topic):
        self.received_messages[topic] = Queue(maxsize=self.queue_size)

    def preprocess_message(self,msg):
        if "header" in msg:
            if "topic" in msg['header']:
                topic = msg['header']['topic']

                if topic == "new_peer":

                if topic == "remove_peer":

                if topic == "heartbeat":


    def execute(self):
        try:
            d = self.socket.recvfrom(self.buffer_size)
            data = d[0].decode()
            addr = d[1]

            msg = self.serializer.deserialize(data)

            self.preprocess_message(msg)

            if 'header' in msg:
                if 'topic' in msg['header']:
                    if msg['header']['topic'] in self.received_messages:
                        topic = msg['header']['topic']
                        self.received_messages[topic].put(msg)

        except:
            print("no incoming messages")

        if not self.outgoing_messages.empty():
            o_msg   = self.outgoing_messages.get()
            o_msg_b = self.serializer.serialize(o_msg)
            o_msg_b = o_msg_b.encode()

            for p in self.peers[o_msg['header']['topic']]:
                self.socket.sendto(o_msg_b,p)

    def get_message(self, topic):
        if topic in self.received_messages:
            if self.received_messages[topic].empty(): return None
            return self.received_messages[topic].get()

        return None

    def send_message(self, data, topic):
        msg = {}
        msg['header'] = {}
        msg['header']['from']  = "{}:{}".format(self.address,self.port)
        msg['header']['topic'] = topic

        msg['data'] = data

        self.outgoing_messages.put(msg)
