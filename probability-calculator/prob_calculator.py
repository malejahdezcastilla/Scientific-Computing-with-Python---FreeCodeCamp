import copy
import random
from collections import Counter

class Hat :
    def __init__(self, **kwargs) :
        self.contents = []
        
        for key, value in kwargs.items () :
            print (key, value)
            self.contents += [key] * value
        print ('\n contents \n', self.contents)
            

    def draw (self, num_balls) :
        if num_balls > len (self.contents) :
            return self.contents

        picked_balls = random.sample (self.contents, num_balls)
        for ball in picked_balls :
            self.contents.remove (ball)
        return picked_balls

def experiment (hat, expected_balls, num_balls_drawn, num_experiments) :
    n = num_experiments
    m = 0

    for i in range (num_experiments) :
        hat_copy = copy.deepcopy(hat)
        selected_balls = hat_copy.draw(num_balls_drawn)

        count_select_balls = Counter (selected_balls)

        common_balls = {}
        for key in count_select_balls:
          
            if (key in expected_balls and count_select_balls[key] >= expected_balls[key]):
                common_balls[key] = expected_balls[key]
  
        if common_balls == expected_balls:
            m += 1
  
    probability = m/n        
   
    return probability  


#def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
