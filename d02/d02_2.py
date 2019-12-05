def set_values(arr, v1, v2):
	arr[1] = v1
	arr[2] = v2

def grouped(iterable, n):
	return zip(*[iter(iterable)]*n)

def run(arr):
	for op, val1, val2, loc in grouped(arr, 4):
		if op == 99:
			break
		elif op == 1:
			arr[loc] = arr[val1] + arr[val2]
		else:
			arr[loc] = arr[val1] * arr[val2]

def main():
	f = open('d02.txt', 'r')
	content = f.read()
	content = content.strip('\n')
	arr = content.split(',')
	arr = [int(x) for x in arr]
	for x in range(0, 100):
		for y in range(0, 100):
			tmp = arr.copy()
			set_values(tmp, x, y)
			run(tmp)
			if (tmp[0] == 19690720):
				print(x * 100 + y)
				exit()

main()