import sys
import collections 


def calculator(number, string):
	for letter in string:
		if letter == 'h':
			number = number//2
		elif letter == 't':
			number = number*3 +1
	return number

def ztalloc(number, Lout, Rout, new_q, seen_l, visited_set):
	while new_q:
		string = new_q.popleft()
		number1 = calculator(number, string)
		#"""
		if (number1 not in visited_set):
			if number1>=Lout and number1 <= Rout:
				seen_l.append(string)
				new_q.append(string + 'h')
				if number1*3+1<=999999:
					new_q.append(string + 't')
				visited_set.add(number1)
			else:
				new_q.append(string + 'h')
				if number1*3+1<=999999:
					new_q.append(string + 't')
				visited_set.add(number1)
		else:
			continue
		
		"""
		if number1>=Lout and number1 <= Rout:
			seen_l.append(string)
			new_q.append(string + 'h')
			if number1*3+1<=999999:
				new_q.append(string + 't')		
		else:
			new_q.append(string + 'h')
			if number1*3+1<=999999:
				new_q.append(string + 't')
		"""
		#"""
		
def main():
	#sys.setrecursionlimit(30000)
	#sys.tracebacklimit = 0
	if len(sys.argv) < 2:
		print("No File Given!")
		sys.exit()

	filename = sys.argv[1]
	file = open(filename, "r")
	if file.mode == 'r':
		contents = file.readlines()
		Q = int(contents[0])
		List = [0]*Q
		for i in range(1, Q+1):
			List[i-1] = [int(x) for x in contents[i].split()]

		for i in List:
			Lin , Rin , Lout , Rout= i[0] , i[1] , i[2] , i[3]
			print(Lin , Rin , Lout , Rout)
			Answerlist = []
			for i in range(Lin, Rin + 1):
				new_q = collections.deque()
				visited_set = set()
				seen_l =  []
				if i>=Lout and i<=Rout:
					seen_l.append("EMPTY")
				new_q.append('h')
				new_q.append('t')
				ztalloc(i, Lout, Rout, new_q, seen_l, visited_set)
				Answerlist.append(seen_l)
			if len(Answerlist)==1:
				if Answerlist[0]:
					print(Answerlist[0][0])
				else:
					print("IMPOSSIBLE")
				continue
			result = set(Answerlist[0][0])
			for s in Answerlist[1:]:
				result.intersection_update(s)
			if result:
				print(min(result))
			else:
				print("IMPOSSIBLE")

if __name__ == '__main__':
	main()