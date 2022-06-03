import copy
from random import randint


class Hat:
    
    def __init__(self, **kwargs):
        self.contents = []
        for k, v in kwargs.items():
            for i in range(v):
                self.contents.append(k)
        print(self.contents)

    def draw(self, numb):
        available = len(self.contents)
        balls = []
        if numb > available:
            return self.contents
        max = len(self.contents)
        values = list()
        for i in range(0, numb):
            while True:
                val = randint(0, max)
                if values.count(val) != 0:
                    val = randint(0, max)
                else: 
                    values.append(val)
                    break
        for c in range(0, len(values)):
            balls.append(self.contents[values[c]])
            self.contents.pop(values[c])
        
        return self.contents