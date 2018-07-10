import time

def do_nothing(x):
    return x

def handler_wrapper(args_dict, func, packer=do_nothing):
    """
    args_to_use - dict - message arg -> func arg
    """
    def handler(message,node):
        args_dict = {}
        for arg in args_dict:
            if arg=="node":
                args_dict[arg]=node
            elif arg=="header":
                args_dict[arg]=msg['header']
            else:
                args_dict[arg]=msg['data'][arg]

        data = func(**args_dict)

        return packer(data)

    return handler

class Node(object):
    def __init__(self, communicator, sleep_time=0.1):
        self.communicator = communicator
        self.sleep_time   = sleep_time

        self.msg_handlers = {}

    def add_handler(self, topic, handler, response_topic=""):
        self.msg_handlers[topic] = {
        "handler":handler,
        "response_topic":response_topic
        }

    def execute(self):
        msg = self.communicator.get_message()
        if msg == None:
            time.sleep(self.sleep_time)
            return

        if not "topic" in msg['header']:
            print("Received message without topic")
            return

        topic = msg['header']['topic']

        if not topic in self.msg_handlers: return

        data = self.msg_handlers[topic]['handler'](message=msg, node=self)

        response_topic = self.msg_handlers[topic]['response_topic']

        if data == None: return

        self.communicator.send_message(data, response_topic)
