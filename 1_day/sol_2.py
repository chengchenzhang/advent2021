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
	sum_3 = p_input.copy()
	for i,x in enumerate(sum_3):
		if i > 1:
			sum_3[i] = sum(p_input[i-2:i+1])
	sum_3 = sum_3[2:]
	shift_1 = sum_3[1:]

	dif_list = [True if a-b > 0 else False for a,b in zip(shift_1,sum_3[:-1])]
	print(dif_list)
	return dif_list.count(True) 

if __name__ == '__main__':
	args = parser.parse_args()
	pro_input = process_input(args.i)
	out = solve(pro_input)
	print(out)
