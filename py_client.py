# -*- coding:utf-8 -*-
__author_='作者'

from thrift.protocol import TCompactProtocol
from thrift.transport import TSocket
from thrift.transport import TTransport

from generated.python import PersonService
from generated.python import ttypes
from thrift import Thrift

try:
    tSocket = TSocket.TSocket('localhost', 8899)
    tSocket.setTimeout(600)

    transport = TTransport.TFramedTransport(tSocket)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    client = PersonService.Client(protocol)

    transport.open()
    person = client.getPersonByUsername("张三")

    print(person.username)
    print(person.age)
    print(person.married)

    print('----------------------')

    newPerson = ttypes.Person()
    newPerson.username = "李四"
    newPerson.age = 30
    newPerson.married = False

    client.savePerson(newPerson)

    transport.close()

except Thrift.TException as ex:
     print(ex.message)