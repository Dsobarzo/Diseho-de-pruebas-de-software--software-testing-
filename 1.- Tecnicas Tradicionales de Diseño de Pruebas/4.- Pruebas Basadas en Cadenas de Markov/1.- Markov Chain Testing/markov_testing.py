import numpy as np

class Markov(object):

    def __init__(self, state_dict):
        self.state_dict = state_dict
        self.state = list(self.state_dict.keys())[0]

    def check_state(self):
        print('Estado actual: %s' % (self.state))

    def set_state(self, state):
        self.state = state
        print('Estado asignado: %s' % (self.state))

    def next_state(self):
        A = self.state_dict[self.state]
        self.state = np.random.choice(a=list(A[0]), p=list(A[1]))
        print('Nuevo estado: %s' % (self.state))