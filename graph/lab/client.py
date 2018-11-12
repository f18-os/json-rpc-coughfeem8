import socket
from bsonrpc import JSONRpc
from bsonrpc.exceptions  import FramingError
from bsonrpc import (
    JSONFramingNetstring, JSONFramingNone, JSONFramingRFC7464)


#cut-the-corners TCP Client:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50001))

rpc = JSONRpc(s,framing_cls = JSONFramingNone)
server =rpc.get_peer_proxy()

#Execute the server

import json

print(server.nop({1:[2,3]}))
request =  open('request.json', 'r')
tree = json.load(request)

print(server.increment(tree))

rpc.close() #closes the socket 's' also
