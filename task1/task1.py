import argparse

parser = argparse.ArgumentParser(description='Sequence build')
parser.add_argument('array_len', metavar='n', type=int, help='size of the circle')
parser.add_argument('step_len', metavar='m', type=int, help='size of the step')
args = parser.parse_args()

class RoundList(list):
	def __getitem__(self, index):
		return super(RoundList, self).__getitem__(index % len(self))


array = RoundList(i + 1 for i in range(args.array_len))
x = 0
while not x or x % args.array_len != 0:
	print(array[x], end='')
	x += args.step_len - 1
print()
