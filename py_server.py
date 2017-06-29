# -*- coding:utf-8 -*-
__author_='作者'

from thrift import Thrift
from thrift.server import TNonblockingServer
from thrift.server import TServer
from thrift.protocol import TCompactProtocol
from thrift.transport import TTransport
from thrift.transport import TSocket


from generated.python import PersonService
from PersonServiceImpl import PersonServiceImpl
import socket
import glob
import sys

try:
    personServiceHandler = PersonServiceImpl()
    processor = PersonService.Processor(personServiceHandler)
    #serverSocket = TSocket.TServerSocket(port=8899)
    #serverSocket = TSocket.TServerSocket(port=8899, socket_family=socket.AF_INET)
    serverSocket = TSocket.TServerSocket(port=8899)
    #serverSocket = TSocket.TServerSocket(host='localhost',port=8899)
    transportFactory = TTransport.TFramedTransportFactory()
    protocolFactory = TCompactProtocol.TCompactProtocolFactory()

    #server = TNonblockingServer.TNonblockingServer(processor, serverSocket, transportFactory, protocolFactory)
    server = TServer.TSimpleServer(processor, serverSocket, transportFactory, protocolFactory)
    server.serve()
except Thrift.TException as ex:
    print(ex.message)