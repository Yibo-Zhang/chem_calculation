import re

class Output(object):
	def __init__(self):
		super(Output,self).__init__()



	####### get optimized structure
	def load_nwoutput(self,dir):
		self.structure = []
		# pattern = re.compile(r'Output coordinates in angstroms')
		start_pattern = re.compile(r'Output')
		end_pattern = re.compile(r'Atomic Mass')
		start_num = 0
		end_num = 0
		with open(dir,'r') as nwoutput:
			lines = nwoutput.readlines()
			for n,i in enumerate(lines):
				start_match = re.search(start_pattern,i)
				if start_match:
					start_num = n
				end_match = re.search(end_pattern,i)
				if end_match:
					end_num = n
			start_num += 4
			end_num -= 1
			self.structure = lines[start_num:end_num]
	def get_structure(self,dir):
		self.load_nwoutput(dir)
		structure = ''
		length = len(self.structure)
		structure = structure + str(length) + '\n\n'
		for i in self.structure:
			words = i.split()
			structure = structure + words[1]+ ' '*4
			structure = structure + words[3]+ ' '*4
			structure = structure + words[4]+ ' '*4
			structure = structure + words[5]+ ' '*4
			structure = structure + '\n'
		name = dir.split('.')[0]
		name +='.xyz'
		with open(name,'a') as f:
			f.write(structure)

	####### get optimized structure

	####### get energy
	def get_energy(self,directory):
		print(directory.split('/')[-2])
		pattern = re.compile(r'DFT energy')
		with open(directory,'r') as nwoutput:
			line = nwoutput.readline()
			while line:
				if re.search(pattern,line):
					print(line,end='\n')
				line = nwoutput.readline()



	def get_all_energy(self,dir):
		from os import walk
		pattern = re.compile(r'.out$')
		outs = []
		for root, dirs, files in walk(dir):
			# print(root)
			# print(dirs)
			# print(files)
			for i in files:
				if re.search(pattern,i):
					outs.append(root+'/'+i)
		for dir in outs:
			self.get_energy(dir)



if __name__ == '__main__':
	# dir = '/Users/Bo/Desktop/restat.out'
	# nwOutPut = Output()
	# nwOutPut.get_structure(dir)
	dir = '/Users/Bo/Desktop/close_gradually'
	nwOutPut = Output()
	nwOutPut.get_all_energy(dir)
