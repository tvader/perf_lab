import argparse

parser = argparse.ArgumentParser(description='Is the point on(0) inside(1) or outside (2) the circle')
parser.add_argument('circle', metavar='c', type=str, help='name of the file with coordinates and radius of the circle')
parser.add_argument('points', metavar='p', type=str, help='name of the file with coordinates of points')
args = parser.parse_args()

with open(args.circle) as f1:
	line = f1.readline()
	c_coords = [float(x) for x in line.split()]
	r = float(f1.readline())
with open (args.points) as f2:
	for line in f2:
		p_coords = ([float(x) for x in line.split()])
		distance = ((p_coords[0] - c_coords[0])**2 + (p_coords[1] - c_coords[1])**2)**0.5
		if distance == r:
			print(0)
		elif distance < r:
			print(1)
		else:
			print(2)
