import os
import sys
sys.path.append(os.path.abspath('..'))

import time

from src.network import serialize, udp
from src.systems import node

def create_node(address, port, serializer, sleep_time=0.1):
    comm = udp.UDP(sleep_time=sleep_time)
    comm.setup(address, port, serializer)
    comm.start()
    n = node.Node(comm)
    return n

def empty_print(x):
    print(x)
    return None

serializer = serialize.JSONSerializer()

node_1 = create_node('',5555,serializer)
node_1.add_handler("world", lambda x: x+" hello", "hello")
node_1.add_handler("world", empty_print)
node_1.communicator.add_peer( ('',6666), "hello" )

node_2 = create_node('',6666,serializer)
node_2.add_handler("hello", lambda x: x+" world", "world")
node_2.add_handler("hello", empty_print)
node_2.communicator.add_peer( ('',5555), "world" )

node_1.communicator.send_message("hello","hello")

node_1.execute()
time.sleep(1)
node_2.execute()
