import numpy as np
import py3Dmol
class Compound(object):
	def __init__(self,name=None):
		super(Compound,self).__init__()
		if name:
			self.name = name
		self._atomNum = 0
		self._atomNames = []
		self._atomPos = []
	def load_xyz(self,filename):
		with open(filename,'r') as xyz_file:
			n_atoms = int(xyz_file.readline())
			xyz_file.readline()
			coords = np.zeros(shape=(n_atoms,3),dtype=np.float64)
			for row, _ in enumerate(coords):
				line = xyz_file.readline().split()
				if not line:
					raise NumberError('Incorrect number of lines in input file')
				coords[row] = line[1:4]
				self._atomNames.append(line[0])
			# Verify we have read the last line by ensuring the next line in blank
			line = xyz_file.readline().split()
			if line:
				msg = ('Incorrect number of lines in input file.')
				raise xyz_Error(msg)
			if not self._atomPos:
				self._atomPos = np.array(coords)
			else:	
				np.concatenate((self._atomPos,coords))
		self._atomNum += n_atoms

	def _formate(self):
		xyz = str(self._atomNum) + '\n'
		for row, coord in enumerate(self._atomPos):
			# print (row,coord)
			xyz = xyz + '\n' + self._atomNames[row] + '    '
			xyz = xyz + '    '.join(str(num) for num in coord) 
		return xyz

	def add_xyz(self,filename):
		pass
	def z_rotate(self,theta):
		pass
	def translate(self,x=0,y=0,z=0):
		pass
	def head(self):
		print(self._atomPos[:10])
	def visualize(self):
		xyz = self._formate()
		xyzview = py3Dmol.view(width=400,height=400)
		xyzview.addModel(xyz,'xyz')
		xyzview.setStyle({'stick':{}})
		xyzview.setBackgroundColor('0xeeeeee')
		xyzview.zoomTo()
		xyzview.show()
	def save(self,filename):
		pass
	def generate_nw(self):
		pass
if __name__ == '__main__':
	CuHHTP = Compound('CuHHTP')
	CuHHTP.load_xyz('./new.xyz')
	CuHHTP.visualize()