import re

class Output(object):
	def __init__(self):
		super(Output,self).__init__()

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


if __name__ == '__main__':
	dir = '/Users/Bo/Desktop/restat.out'
	nwOutPut = Output()
	nwOutPut.get_structure(dir)
