import argparse

parser = argparse.ArgumentParser(description='Sequence build')
parser.add_argument('array', metavar='c', type=str, help='name of the file with array')
args = parser.parse_args()

array = []
with open(args.array) as f:
	for line in f:
		array.append(int(line))
sum = 0;
for x in array:
	sum += x
average = sum // len(array)
shortway = 0
for x in array:
	shortway += abs(x - average)
print(shortway)
