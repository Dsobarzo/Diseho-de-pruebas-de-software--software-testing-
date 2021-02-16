import numpy as np
from markov_testing import *

state_dict = {'A': np.array([['A', 'B', 'C'],
                             [.2, .4, .4]]),
              'B': np.array([['A', 'C'],
                             [.4, .6]]),
              'C': np.array([['A', 'B'],
                             [.6, .4]])}



diagram_a = Markov(state_dict)
diagram_a.check_state()
diagram_a.set_state('B')
for x in range(10):
    diagram_a.next_state()




