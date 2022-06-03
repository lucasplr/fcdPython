import copy
import random


class Hat:
    
    def __init__(self, **kwargs):
        print(kwargs)
        self.contents = []
        for k, v in kwargs.items():
            for i in range(v):
                self.contents.append(k)
        print(self.contents)
