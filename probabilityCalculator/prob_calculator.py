import copy
import random


class Hat:
    
    def __init__(self, **kwargs):
        self.contents = []
        for k, v in kwargs.items():
            for i in range(v):
                self.contents.append(k)
        print(self.contents)

    def draw(self, numb):
        balls = []
        if (numb > len(self.contents)):
            return self.contents
        for i in range(numb):
            val = self.contents.pop(int(random.random() * len(self.contents)))
            balls.append(val)
        return balls

def experiments(hat, expected_balls, num_balls_draw, num_experiments):
    count = 0
    for i in range (num_experiments):
        expected_copy = copy.deepcopy(expected_balls)
        hat_copy = copy.deepcopy(hat)
        colors_gotten = hat_copy.draw(num_balls_draw)
    
    for color in colors_gotten:
        if (color in expected_copy):
            expected_copy[color]-=1

    if(all(x <= 0 for x in expected_copy.values())):
        count += 1
    return count / num_experiments