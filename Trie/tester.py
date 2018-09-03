import os
import sys
import filecmp
import time

def trunc(x):
	return int(x * 1000) / 1000

if __name__ == "__main__":
	results = open("Benchmark.txt", "w")
	no_inputs = 0
	for file in os.listdir("./Inputs/"):
		if file.endswith(".in"):
			no_inputs += 1
	c_time = 0
	py_time = 0
	for test in range(0, no_inputs):
		results.write("Test " + str(test) + ":\n")

		start = time.time()
		os.system(".\C++\main_c++ " + str(test))
		elapsed = trunc(time.time() - start)
		results.write("C++ time : " + str(elapsed) + '\n')
		c_time += elapsed

		start = time.time()
		os.system("python ./Python/main_python.py " + str(test))
		elapsed = trunc(time.time() - start)
		results.write("Python time : " + str(elapsed) + '\n')
		py_time += elapsed

		if filecmp.cmp("./Outputs/output_" + str(test) + "_python.out", "./Outputs/output_" + str(test) + "_c++.out") == False:
			print("Test ", test, " has different output")
		results.write("-" * 30 + '\n')

	results.write("C++ total time : " + str(c_time) + '\n')
	results.write("Python total time : " + str(py_time) + '\n')

	results.write("-" * 30 + '\n')
	results.write("C++ average time : " + str(trunc(c_time / no_inputs)) + '\n')
	results.write("Python average time : " + str(trunc(py_time / no_inputs)) + '\n')
