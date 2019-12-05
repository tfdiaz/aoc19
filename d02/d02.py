def set_values(arr):
	arr[1] = 12
	arr[2] = 2

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
	set_values(arr)
	run(arr)
	print(arr[0])
	f.close

main()