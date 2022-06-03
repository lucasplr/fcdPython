import copy
import random


class Hat:
    
    def __init__(self, **kwargs):
        print(kwargs)
        content = []
        for c in range(0, len(kwargs)):
            content.append(kwargs)
        print(content)
