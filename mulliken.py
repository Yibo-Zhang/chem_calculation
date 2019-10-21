import re

class Mulliken(object):
	def __init__(self):
		super(Mulliken,self).__init__()

	####### get optimized structure
	def get_structure(self,dir,title,start_pattern,end_pattern):
		self.structure = []
		# pattern = re.compile(r'Output coordinates in angstroms')
		start_pattern = re.compile(r'Total Density - Mulliken Population Analysis')
		end_pattern = re.compile(r'Atom       Charge   Shell Charges')
		start_num = 0
		switch = False
		with open(dir,'r') as nwoutput:
			lines = nwoutput.readlines()
			for n,i in enumerate(lines):
				start_match = re.search(start_pattern,i)
				if start_match:
					start_num = n
					switch = True
				end_match = re.search(end_pattern,i)
				if end_match and switch:
					end_num = n
					switch = False
			start_num += 5
			end_num -= 1
			self.structure = lines[start_num:end_num]
		structure = ''
		length = len(self.structure)
		current_atom_number = '1'
		current_atom_charge = 0
		current_atom = self.structure[0].split()[3]
		with open('/Users/Bo/Desktop/result','a') as f:
			f.write(title+'\n\n')
		for i in self.structure:
			words = i.split()
			if words[2] == current_atom_number:
				current_atom_charge += float(words[1])
			else:
				with open('/Users/Bo/Desktop/result','a') as f:
					f.write(str(current_atom_number) + ' '*4 + current_atom + ' '*4 + str(current_atom_charge)+'\n')
				current_atom = words[3]
				current_atom_number = words[2]
				current_atom_charge = float(words[1])
		with open('/Users/Bo/Desktop/result','a') as f:
			f.write(str(current_atom_number) + ' '*4 + current_atom + ' '*4 + str(current_atom_charge)+'\n')
	def get_all_charge(self,dir):
		start_pattern = re.compile(r'Total Density - Mulliken Population Analysis')
		end_pattern = re.compile(r'Atom       Charge   Shell Charges')
		self.get_structure(dir,'-'*20+'\nTotal Density\n'+'-'*20,start_pattern,end_pattern)

		start_pattern = re.compile(r'Spin Density - Mulliken Population Analysis')
		end_pattern = re.compile(r'Atom       Charge   Shell Charges')
		self.get_structure(dir,'\n'+'-'*20+'\nSpin Density\n'+'-'*20,start_pattern,end_pattern)

	# def get_energy(self,directory):
	# 	print(directory.split('/')[-2])
	# 	pattern = re.compile(r'DFT energy')
	# 	with open(directory,'r') as nwoutput:
	# 		line = nwoutput.readline()
	# 		while line:
	# 			if re.search(pattern,line):
	# 				print(line,end='\n')
	# 			line = nwoutput.readline()
	# def get_all_energy(self,dir):
	# 	from os import walk
	# 	pattern = re.compile(r'.out$')
	# 	outs = []
	# 	for root, dirs, files in walk(dir):
	# 		for i in files:
	# 			if re.search(pattern,i):
	# 				outs.append(root+'/'+i)
	# 	for dir in outs:
	# 		self.get_energy(dir)



if __name__ == '__main__':
	dir = '/Users/Bo/Desktop/mulliken.out'
	Mulliken = Mulliken()
	Mulliken.get_all_charge(dir)
