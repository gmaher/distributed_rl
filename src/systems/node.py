import time

class Node(object):
    def __init__(self, receiver, broadcaster, serializer, sleep_time=0.1):
        self.receiver     = receiver
        self.broadcaster  = broadcaster
        self.serializer   = serializer
        self.sleep_time   = sleep_time

        self.msg_handlers = {}

    def add_handler(topic, handler):
        self.msg_handlers[topic] = handler

    def execute(self):
        msg = self.receiver.get_message()
        if msg == None:
            time.sleep(self.sleep_time)
            return

        if not "subject" in msg:
            print("Received message without subject")
            return

        data = self.msg_handlers[msg.topic](message=msg, node=self)

        resp = self.serializer.serialize(data)

        self.broadcaster.send_message(resp)
