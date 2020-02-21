def get_boundary_xyz(file):
	with open(file) as f:
		xyz = f.readlines()[2:]
	x = [i.split()[1] for i in xyz]
	y = [i.split()[2] for i in xyz]
	z = [i.split()[3] for i in xyz]

	print('x range is:',max(x),'    ',min(x))
	print('y range is:',max(y),'    ',min(y))
	print('z range is:',max(z),'    ',min(z))


if __name__ == '__main__':
	file = 'Please input the file directory'
	get_boundary_xyz(file)




