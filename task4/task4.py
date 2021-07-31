import argparse

parser = argparse.ArgumentParser(description='Finding the shortests way to bring numbers to common value')
parser.add_argument('array', metavar='c', type=str, help='name of the file with array')
args = parser.parse_args()

array = []
with open(args.array) as f:
	for line in f:
		array.append(int(line))
sum = 0;
for x in array:
	sum += x
average = round(sum / len(array))
average1 = min(array)
average2 = max(array)
shortway = 0
shortway1 = 0
shortway2 = 0
for x in array:
	shortway += abs(x - average)
	shortway1 += abs(x - average1)
	shortway2 += abs(x - average2)
print(min(shortway, shortway1, shortway2))
