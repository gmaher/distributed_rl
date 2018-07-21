import os
import sys
sys.path.append(os.path.abspath('..'))

import time

from comm import serialize, udp


serializer = serialize.JSONSerializer()


comm1 = udp.UDP(sleep_time=1)
comm1.setup("", 5555, serializer)
comm1.add_peer(("localhost",6666), "")

comm2 = udp.UDP(sleep_time=1)
comm2.setup("", 6666, serializer)

comm1.send_message("hello","hello")
o_msg = comm1.outgoing_messages.get()
print(o_msg)
o_msg_b = serializer.serialize(o_msg).encode()
print(o_msg_b)

#comm1.socket.sendto(o_msg_b,("localhost",6666))

try:
    d = comm2.socket.recvfrom(4096)
    print(d)
    print(d[0].decode())
except:
    print("no incoming messages")

print("finished")
