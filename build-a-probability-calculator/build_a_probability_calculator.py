import copy
import random

class Hat:
    def __init__(self, **kwargs):
        i = kwargs.items()
        self.contents = [k for k, v in i for _ in range(v)]

    def draw(self, nballs):
        hballs = self.contents
        res = []

        if nballs > len(hballs):
            for i in range(len(hballs)):
                r = random.randrange(len(hballs))
                res.append(hballs[r])
                del hballs[r]

            return res

        for i in range(nballs):
            r = random.randrange(len(hballs))
            res.append(hballs[r])
            del hballs[r]

        return res

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass

test = Hat(yellow=3, blue=2, green=6)
# print(test.contents)
print(test.draw(11))