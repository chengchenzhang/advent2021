#Processing input
import argparse

parser = argparse.ArgumentParser(description='Takes in input files')
parser.add_argument('-i', type=str, required=True)

def process_input(input_file):
	prob_input = []

	with open(input_file, 'r') as f:
		for line in f:
			line = line[:-1].split(',')
			prob_input.append(line)
	prob_input = [int(x) for x in prob_input[0]]
	return prob_input

#Problem Solving
def solve(p_input):
	print(p_input)
	f_dict = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
	for fish in p_input:
		f_dict[fish] = f_dict[fish] + 1
	for i in range(256):
		new_fish = f_dict[0]
		for i in range(0,8):
			f_dict[i] = f_dict[i+1]
		f_dict[6] = f_dict[6] + new_fish
		f_dict[8] = new_fish
		print(f_dict)
	out = 0
	for k,v in f_dict.items():
		out += v
	return out

if __name__ == '__main__':
	args = parser.parse_args()
	pro_input = process_input(args.i)
	out = solve(pro_input)
	print(out)
