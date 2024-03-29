import socket
from bsonrpc import JSONRpc
from bsonrpc import request, service_class
from bsonrpc.exceptions import FramingError
from bsonrpc.framing import (
	JSONFramingNetstring, JSONFramingNone, JSONFramingRFC7464)
import sys
sys.path.append('../')
import json

# class providing functions for the client use:
@service_class
class ServerServices(object):

    @request
    def nop(self,txt):
        print (txt)
        return txt

    
    #helper method
    def increment_helper(self,graph):
        graph['value'] += 1
        for child in graph['children']:
            child = self.increment_helper(child)
        return graph

    #augment the items on the node
    @request
    def increment(self,graph):
        print (graph)
        graph = self.increment_helper(graph)
        return graph


#Quick-and-dirty TCP Server:
ss = socket.socket(socket.AF_INET, socket. SOCK_STREAM)
ss.bind(('localhost',50001))
ss.listen(10)

#run the sever
while True:
    s, _ =ss.accept()
    #JSONRcp object spawns internal thread to serve the connection.
    JSONRpc(s, ServerServices(), framing_cls = JSONFramingNone)

