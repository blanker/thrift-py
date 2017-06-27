# -*- coding:utf-8 -*-
__author__ = '作者'

from generated.python import ttypes

class PersonServiceImpl:
    def getPersonByUsername(self, username):
        print("Got client param: " + username)

        person = ttypes.Person()
        person.married = False
        person.age = 25
        person.username = "王五"

        return person

    def savePerson(self, person):
        print("Got client param: ")
        print(person.username)
        print(person.age)
        print(person.married)