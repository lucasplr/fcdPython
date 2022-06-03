import copy
import random


class Hat:
    
    def __init__(self, **kwargs):
        self.contents = []
        for k, v in kwargs.items():
            for i in range(v):
                self.contents.append(k)

    def draw(self, numb):
        balls = []
        if (numb > len(self.contents)):
            return self.contents
        else:
            for i in range(numb):
                val = random.sample(self.contents, 1)
                balls += val
                for ball in val:
                    if ball in self.contents:
                        self.contents.remove(ball)
        return balls

def experiments(hat, expected_balls, num_balls_draw, num_experiments):
    count = 0
    expected_list = []
    for c, n in expected_balls.items():
        for j in range(n):
            expected_list.append(c)
    new_hat = copy.deepcopy(hat)
    sample_list = new_hat.draw(num_balls_draw)
    for color in sample_list:
        if color in expected_list:
            expected_list.remove(color)
    if len(expected_list) == 0:
        count += 1
    prob = count / num_experiments
    return prob

