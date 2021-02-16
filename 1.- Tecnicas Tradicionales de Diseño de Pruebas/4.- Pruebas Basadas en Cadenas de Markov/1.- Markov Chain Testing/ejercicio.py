from markov_testing import *


estados = {'inicio':np.array([['incompleto'],[1.0]]),
           'incompleto': np.array([['completo','ilocalizable'], [0.8,0.2]]),
           'completo': np.array([['reprogramado','ruteado'], [0.1,0.9]]),
           'ilocalizable': np.array([['completo'], [1.0]]),
           'reprogramado': np.array([['ruteado'], [1.0]]),
           'ruteado': np.array([['reprogramado','confirmado','ruteado'], [0.2,0.5,0.3]]),
           'confirmado': np.array([['confirmado'], [1.0]])}


diagram_a = Markov(estados)
diagram_a.set_state('inicio')
diagram_a.check_state()


for x in range(20):
    print("----------------------------------------------------------")
    diagram_a.set_state('inicio')
    while diagram_a.state != 'confirmado':
        diagram_a.next_state()
