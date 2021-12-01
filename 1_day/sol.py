#Processing input
import argparse

parser = argparse.ArgumentParser(description='Takes in input files')
parser.add_argument('-i', type=str, required=True)

def process_input(input_file):
	prob_input = []

	with open(input_file, 'r') as f:
		for line in f:
			prob_input.append(int(line))

	return prob_input

#Problem Solving
def solve(p_input):
	shift_1 = p_input[1:]
	dif_list = [ True if a-b > 0 else False for a,b in zip(shift_1,p_input[:-1])]
	return dif_list.count(True)

if __name__ == '__main__':
	args = parser.parse_args()
	pro_input = process_input(args.i)
	out = solve(pro_input)
	print(out)
