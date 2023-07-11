#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super()._init__(first_name, last_name)
        self.knowledge = []
        
    
    def learn(self):
       pass