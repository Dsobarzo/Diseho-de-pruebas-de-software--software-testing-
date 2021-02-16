from fuzzbang.alphanumericfuzzer import AlphaNumericFuzzer

N = 10 #numero de pruebas

# fronteras de la longitud de las cadenas a generar 
MIN_LEN = 0
MAX_LEN = 8

f = AlphaNumericFuzzer(MIN_LEN, MAX_LEN) # fuzzor 

# genera los ejemplos 
for i in range(N):
    data = f.generate() # genera la cadena 
    print("(" + str(len(data)) + ")") # muestra la longitud de la cadena 
    print(data) # imprime la cadena 
