#Processing input
import argparse

parser = argparse.ArgumentParser(description='Takes in input files')
parser.add_argument('-i', type=str, required=True)

def process_input(input_file):
	prob_input = []

	with open(input_file, 'r') as f:
		for line in f:
			line = line[:-1].split(' -> ')
			line = [ x.split(',') for x in line]
			prob_input.append(line)
	print(prob_input)
	return prob_input

def gen_points(point_set):
	out = []
	x1 = int(point_set[0][0])
	y1 = int(point_set[0][1])
	x2 = int(point_set[1][0])
	y2 = int(point_set[1][1])
	ymax = y1 if y1 > y2 else y2
	ymin = y1 if y1 < y2 else y2

	xmax = x1 if x1 > x2 else x2
	xmin = x1 if x1 < x2 else x2
	if x1 != x2 and y1 != y2:
		x_step = 1 if x1 < x2 else -1
		y_step = 1 if y1 < y2 else -1
		dif = abs(x1 - x2)
		for i in range(dif+1):
			out.append((x1 + x_step*i,y1 + y_step*i))
		return out
	if x1 == x2:
		for i in range(ymin,ymax+1):
			out.append((x1,i))
	elif y1 == y1:
		for i in range(xmin,xmax+1):
			out.append((i,y1))
	return out
#Problem Solving
def solve(p_input):
	board = {}
	for p in p_input:
		l1 = gen_points(p)
		print(l1)
		for p in l1:
			if p not in board:
				board[p] = 1
			else:
				board[p] = board[p] + 1
	out = 0
	print(len(board))
	for i in board.items():
		if i[1] > 1:
			out += 1
	return out

if __name__ == '__main__':
	args = parser.parse_args()
	pro_input = process_input(args.i)
	out = solve(pro_input)
	print(out)
