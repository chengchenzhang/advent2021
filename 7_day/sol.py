#Processing input
import argparse

parser = argparse.ArgumentParser(description='Takes in input files')
parser.add_argument('-i', type=str, required=True)

def process_input(input_file):
	prob_input = []

	with open(input_file, 'r') as f:
		for line in f:
			line = line[:-1].split(',')
			line = [int(x) for x in line]
			prob_input = line

	return prob_input
def is_min(p_input, point, mag_list):
	dif_list = [mag_list[abs(point - x)] for x in p_input]
	dif_p1 = [mag_list[abs(point+1 - x)] for x in p_input]
	dif_m1 = [mag_list[abs(point-1 - x)] for x in p_input]
	s_l = sum(dif_list)
	s_p1 = sum(dif_p1)
	s_m1 = sum(dif_m1)
	return [s_l, s_p1, s_m1]
#Problem Solving
def solve(p_input):
	mass_dict = {}
	min_r = min(p_input)
	max_r = max(p_input)

	mag_list = [0]*(max_r+1)
	for i in range(1,max_r+1):
		mag_list[i] = mag_list[i-1] + i

	point = int((min_r + max_r) /2)
	out = 0
	while True:
		dif = is_min(p_input, point, mag_list)
		print(point, min_r,max_r, dif)
		if dif[0] < dif[1] and dif[0] < dif[2]:
			out = dif[0]
			break
		elif dif[1] < dif[0]:
			min_r = point + 1
		elif dif[2] < dif[0]:
			max_r= point - 1
		point = int((min_r + max_r) /2)
	return out

if __name__ == '__main__':
	args = parser.parse_args()
	pro_input = process_input(args.i)
	out = solve(pro_input)
	print(out)
