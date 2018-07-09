import time

def do_nothing(x):
    return x

def handler_wrapper(args_to_use, func, packer=do_nothing):
    def handler(msg,node):
        args_dict = {}
        for arg in args_to_use:
            if arg=="node":
                args_dict[arg]=node
            else:
                args_dict[arg]=msg[arg]

        data = func(**args_dict)

        
    return handler

class Node(object):
    def __init__(self, communicator, sleep_time=0.1):
        self.communicator = communicator
        self.serializer   = serializer
        self.sleep_time   = sleep_time

        self.msg_handlers = {}

    def add_handler(topic, handler, response_topic=""):
        self.msg_handlers[topic] = {
        "handler":handler,
        "response_topic":response_topic
        }

    def execute(self):
        msg = self.communicator.get_message()
        if msg == None:
            time.sleep(self.sleep_time)
            return

        if not "subject" in msg:
            print("Received message without subject")
            return

        if not msg['topic'] in self.msg_handlers: return

        data = self.msg_handlers[msg.topic]['handler'](message=msg, node=self)
        response_topic = self.msg_handlers[msg.topic]['response_topic']

        if data == None: return

        self.broadcaster.send_message(data, response_topic)
