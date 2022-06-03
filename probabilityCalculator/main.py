import prob_calculator
from prob_calculator import Hat
from prob_calculator import experiments
from unittest import main

hat = Hat(black=6, red=4, green=3)
#hat2 = Hat(red=5, orange=4)
#hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)


hat.draw(1)

prob = experiments(hat=hat, expected_balls={'red': 2, 'green': 1}, num_balls_draw=5, num_experiments=2000)
print('Probability: ', prob)


main(module='test_module', exit=False)