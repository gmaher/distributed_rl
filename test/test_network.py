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

    return comm

# def f1(message, node):
#     s = message['data']['x']
#
#     s = s+' hello'
#     print(s)
#     return {"x":s}
#
# def f2(message, node):
#     s = message['data']['x']
#
#     s = s+' world'
#     print(s)
#     return {"x":s}

serializer = serialize.JSONSerializer()

node_1 = create_node('',5555,serializer)
node_1.add_peer( ('',6666), "hello" )
node_1.subscribe('world')

node_2 = create_node('',6666,serializer)
node_2.add_peer( ('',5555), "world" )
node_2.subscribe('hello')

node_1.send_message({"x":"hello"},"hello")

time.sleep(1)

print(node_2.get_message('hello'))
