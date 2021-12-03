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

def solve(p_input):
	nd_in = [ [int(c) for c in x] for x in p_input]
	np_in = np.array(nd_in)
	np_rot = np.rot90(np_in, -1)

	half = len(np_rot[0])/2
	print(half)
	gamma = ['1' if np.sum(x) > half else '0' for x in np_rot]
	eps = ['0' if x == '1' else '1' for x in gamma]
	gamma = int(''.join(gamma),2)
	eps = int(''.join(eps),2)
	return gamma * eps

if __name__ == '__main__':
	args = parser.parse_args()
	pro_input = process_input(args.i)
	out = solve(pro_input)
	print(out)
