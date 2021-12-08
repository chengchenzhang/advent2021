#Processing input
import argparse
import itertools
parser = argparse.ArgumentParser(description='Takes in input files')
parser.add_argument('-i', type=str, required=True)

def process_input(input_file):
	prob_input = []

	with open(input_file, 'r') as f:
		for line in f:
			prob_input.append(line[:-1].split(' | '))

	return prob_input

#Problem Solving
def solve(p_input):
	_0 = ('a','b','c','f','e','g')
	_1 = ('c','f')
	_2 = ('a','c','d','e','g')
	_3 = ('a','c','d','f','g')
	_4 = ('b','c','d','f')
	_5 = ('a','b','d','f','g')
	_6 = ('a','b','d','e','f','g')
	_7 = ('a','c','f')
	_8 = ('a','b','c','d','e','f','g')
	_9 = ('a','b','c','d','f','g')
	nums = [_0,_1,_2,_3,_4,_5,_6,_7,_8,_9]

	mixed_in = p_input[0].split(' ')
	num_map = {}
	sol_match = {}
	#match 1 
	for num in mixed_in: 
		if len(num) == 2: 
			num_map[_1] = num 
		elif len(num) == 3: 
			num_map[_7] = num 
		elif len(num) == 4:
			num_map[_4] = num
	
	seen = ''
	sol_match['c'] = num_map[_1]
	sol_match['f'] = num_map[_1]
	seen = seen + num_map[_1]
	for c in num_map[_7]:
		if c not in num_map[_1]:
			sol_match[('a')] = c
			seen = seen + c
			break
	
	sol_match['b'] = ''
	sol_match['d'] = ''
	for c in num_map[_4]:
		if c not in num_map[_1]:
			sol_match['b'] = sol_match['b'] + c
			sol_match['d'] = sol_match['d'] + c
			seen = seen + c
	
	sol_match['e'] = ''
	sol_match['g'] = ''
	for c in _8:
		if c not in seen:
			sol_match['e'] = sol_match['e'] + c
			sol_match['g'] = sol_match['g'] + c
			seen = seen + c

	let_match = []
	for k,v in sol_match.items():
		t = []
		for c in v:
			t.append([k,c])
		let_match.append(t)

	p_matches = itertools.product(*let_match)
	def is_unique(mapping):
		seen = []
		for m in mapping:
			if m[1] in seen:
				return False
			seen.append(m[1])
		return True
	p_unique = [list(p) for p in list(p_matches) if is_unique(p)]
	#print(p_unique)
	def make_mapping(mapping):
		m = {}
		for p in mapping:
			m[p[0]] = p[1]
		new_num = []
		for n in nums:
			map_num = ''
			for c in n:
				map_num = map_num + m[c]
			new_num.append(set(map_num))
		mixed_in_set = [set(a) for a in mixed_in]
		matches = [True if n in mixed_in_set else False for n in new_num] 
		if matches.count(True) == 10:
			return True
		return False
	solved_mapping = {}
	for mapping in p_unique:
		if make_mapping(mapping):
			solved_mapping = mapping
			
	out_numbers = p_input[1].split(' ')
	def unscramble(num, mapping):
		m = {}
		for p in mapping:
			m[p[1]] = p[0]
		new_num = []
		for n in num:
			map_num = ''
			for c in n:
				map_num = map_num + m[c]
			new_num.append(set(map_num))
		return new_num
	unscrambled_nums = unscramble(out_numbers,solved_mapping )
	set_nums = [set(n) for n in nums]
	sol = [set_nums.index(n) for n in unscrambled_nums]
	return sol

if __name__ == '__main__':
	args = parser.parse_args()
	pro_input = process_input(args.i)
	out = [solve(input_) for input_ in pro_input]
	out_f = []
	for n in out:
		for m in n:
			out_f.append(m)
	p_1 = [1,4,7,8]
	p_1 = sum([out_f.count(n) for n in p_1])
	print(p_1)
	out_2 = [] 
	for n in out:
		str_l = [str(c) for c in n]
		out_2.append(int(''.join(str_l)))
	print(sum(out_2))
