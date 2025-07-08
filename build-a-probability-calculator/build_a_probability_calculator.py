import copy
import random

class Hat:
    def __init__(self, **kwargs):
        items = kwargs.items()
        self.contents = [k for k, v in items for _ in range(v)]

    def draw(self, n_balls):
        h_balls = self.contents
        res = []

        if n_balls > len(h_balls):
            for i in range(len(h_balls)):
                r = random.randrange(len(h_balls))
                res.append(h_balls[r])
                del h_balls[r]

            return res

        for i in range(n_balls):
            r = random.randrange(len(h_balls))
            res.append(h_balls[r])
            del h_balls[r]

        return res

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    print('hat:', hat.contents)
    print('expected_balls:', expected_balls)
    print('num_balls_drawn:', num_balls_drawn)
    print('num_experiments:', num_experiments)
    M = 0
    t_balls = num_experiments * num_balls_drawn
    for exp in range(num_experiments):
        cp = copy.deepcopy(hat)
        d_balls = cp.draw(num_balls_drawn)
        print(f'experiment #{exp + 1}:\n {d_balls}')
    print('t_balls:', t_balls)

'''
hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

print(hat1.draw(4))
print(hat2.draw(40))
print(hat3.draw(6))
'''
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)
