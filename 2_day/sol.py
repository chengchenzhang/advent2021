#Processing input
import argparse

parser = argparse.ArgumentParser(description='Takes in input files')
parser.add_argument('-i', type=str, required=True)

def process_input(input_file):
	prob_input = []

	with open(input_file, 'r') as f:
		for line in f:
			prob_input.append(line[:-1].split(" "))
	print(prob_input)
	return prob_input

#Problem Solving
def solve(p_input):
	depth = 0
	hor = 0
	aim = 0
	for command in p_input:
		mag = int(command[1])
		if command[0] == 'down':
			aim += int(command[1])
		elif command[0] == 'up':
			aim -= int(command[1])
		elif command[0] == 'forward':
			hor += mag
			depth += aim*mag
	print(hor,depth)
	return hor*depth

if __name__ == '__main__':
	args = parser.parse_args()
	pro_input = process_input(args.i)
	out = solve(pro_input)
	print(out)
