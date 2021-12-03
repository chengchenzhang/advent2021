#Processing input
import argparse
import numpy as np
parser = argparse.ArgumentParser(description='Takes in input files')
parser.add_argument('-i', type=str, required=True)

def process_input(input_file):
	prob_input = []

	with open(input_file, 'r') as f:
		for line in f:
			prob_input.append(line[:-1])

	return prob_input

#Problem Solving
def rating_2(nd_in, comp):
	for i in range(len(nd_in[0])):
		ones = []
		zeros = []
		for x in nd_in:
			if x[i] == 0:
				zeros.append(x)
			else:
				ones.append(x)
		#nd_in = ones if len(ones) >= len(zeros) else zeros
		nd_in = comp(ones,zeros)
		#print('ones', ones)
		#print('zeros', zeros)
		if(len(nd_in) == 1):
			break
	nd_str = ''.join([str(c) for c in nd_in[0]])
	nd_int = int(nd_str,2)
	return nd_int

def solve(p_input):
	nd_in = [ [int(c) for c in x] for x in p_input]
	co2_in = nd_in.copy()
	nd_in = rating_2(nd_in, lambda a,b: a if len(a) >= len(b) else b)
	co2_in = rating_2(co2_in, lambda a,b: b if len(b) <= len(a) else a)
	print(nd_in,co2_in)
	return nd_in*co2_in

	return 0
if __name__ == '__main__':
	args = parser.parse_args()
	pro_input = process_input(args.i)
	out = solve(pro_input)
	print(out)
