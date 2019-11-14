import re

class Output(object):
	def __init__(self):
		super(Output,self).__init__()
	####### get optimized structure
	def load_nwoutput(self,dir):
		self.structure = []
		self.begin_number = 0
		self.end_number=0
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
					self.begin_number +=1
				end_match = re.search(end_pattern,i)
				if end_match:
					end_num = n
					self.end_number +=1
				if self.begin_number and self.end_number and self.begin_number==self.end_number:
					start_num += 4
					end_num -= 1
					self.structure = lines[start_num:end_num]
					self.save_trajectory(self.begin_number)
	def save_trajectory(self,number):
		structure = ''
		length = len(self.structure)
		structure = structure + str(length) + '\n\n'
		for i in self.structure:
			words = i.split()
			print(words)
			structure = structure + words[1]+ ' '*4
			structure = structure + words[3]+ ' '*4
			structure = structure + words[4]+ ' '*4
			structure = structure + words[5]+ ' '*4
			structure = structure + '\n'
		name = 'test'
		with open(name+'_'+str(number)+'.xyz','a') as f:
			f.write(structure)
if __name__ == '__main__':
	out = Output()
	out.load_nwoutput('/Users/Bo/Desktop/trajectory/start.out')
	