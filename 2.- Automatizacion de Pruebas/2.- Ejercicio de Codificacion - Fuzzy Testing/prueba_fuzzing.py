import sys
from mph.program import Program
from fuzzbang.alphanumericfuzzer import AlphaNumericFuzzer

PATH_TO_NAME = "./nombre" # ruta de la aplicacion

def run(string):
	"""
	enviamos la cadena al programa y obtenemos de regreso el valor arrojado
	"""
	prog = Program(PATH_TO_NAME, [])
	prog.append_string_stdin(string)
	prog.exec()
	
	return prog.retval

def generate_input(n):
	"""
	Genera una cadena aleatoria de tamaño n
	"""
	fuzzer = AlphaNumericFuzzer(0, n)
	
	return fuzzer.generate()

if __name__ == "__main__":

	if len(sys.argv) != 3:
		print("uso: python3 fuzztut.py num_ej max_long")
		exit(1)
		
	# linea de comandos
	num_cases = int(sys.argv[1])
	max_length = int(sys.argv[2])
	   
	results = []
	

	for i in range(num_cases):
		input = generate_input(max_length) # genera la entrada del programa
		return_value = run(input) # ejecuta el programa con la entrada generada
		
		# guardamos los resultados de las pruebas
		test_result = {}
		test_result["num"] = i
		test_result["input"] = input
		test_result["output"] = return_value
		results.append(test_result)

	# resumen
	for test in results:
		print("Caso #{:d}:".format(test["num"]))
		print("	IN: " + test["input"])
		print("	OUT: {:4d}".format(test["output"]))
		print("\n")
