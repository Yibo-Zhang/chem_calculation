import numpy as np
import py3Dmol
import os
import math
import sys

class Compound(object):
	def __init__(self,name=None):
		super(Compound,self).__init__()
		if name:
			self.name = name
		self._atomNum = 0
		self._atomNames = []
		self._atomPos = np.array([])
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
			if not self._atomPos.any():
				self._atomPos = np.array(coords)
			else:	
				self._atomPos = np.vstack((self._atomPos,coords))
		self._atomNum += n_atoms

	def _formate(self):
		xyz = str(self._atomNum) + '\n'
		for row, coord in enumerate(self._atomPos):
			# print (row,coord)
			xyz = xyz + '\n' + self._atomNames[row] + '    '
			xyz = xyz + '    '.join(str(num) for num in coord) 
		return xyz

	def add(self,object):
		pass
	def translate(self,x=0,y=0,z=0):
		move = np.array([x,y,z])
		self._atomPos += move
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
		xyz = self._formate()
		with open(filename,'w') as xyz_file:
			xyz_file.write(xyz)

	def generate_nw(self,filename=None):
		if not filename:
			filename = self.name
		cpw = os.path.abspath(os.path.dirname(__file__))
		path = "./{}".format(filename)
		os.mkdir(path);
		self.save('./{}'.format(filename)+'/'+filename+'.xyz')
		with open(cpw+'/energy-dft.nw','r') as nwfile:
			nwcontent = nwfile.read().format(filename,filename,filename+'.xyz')
		with open('./{}'.format(filename)+'/'+filename+'.nw','w') as nwfile:
			nwfile.write(nwcontent)
	def _get_info(self):
		return self._atomNum, self._atomNames, self._atomPos
	def add_molecule(self,molecule):
		Num, Names, Pos = molecule._get_info()
		self._atomNum += Num
		self._atomNames.extend(Names)
		if not self._atomPos.any():
			self._atomPos = Pos
		else:	
			self._atomPos = np.vstack((self._atomPos,Pos))
		# self._atomPos = np.vstack((self._atomPos,Pos))
	def rotation_matrix(self, axis, theta):
	    """
	    Return the rotation matrix associated with counterclockwise rotation about
	    the given axis by theta radians.
	    """
	    axis = np.asarray(axis)
	    axis = axis / math.sqrt(np.dot(axis, axis))
	    a = math.cos(theta / 2.0)
	    b, c, d = -axis * math.sin(theta / 2.0)
	    aa, bb, cc, dd = a * a, b * b, c * c, d * d
	    bc, ad, ac, ab, bd, cd = b * c, a * d, a * c, a * b, b * d, c * d
	    return np.array([[aa + bb - cc - dd, 2 * (bc + ad), 2 * (bd - ac)],
	                     [2 * (bc - ad), aa + cc - bb - dd, 2 * (cd + ab)],
	                     [2 * (bd + ac), 2 * (cd - ab), aa + dd - bb - cc]])
	def z_rotate(self,theta):
		"""
		one lap is 2π.
		"""
		axis = [0, 0, 1]
		self._atomPos=np.dot(self._atomPos,self.rotation_matrix(axis, theta))
	def x_rotate(self,theta):
		axis = [1, 0, 0]
		self._atomPos=np.dot(self._atomPos,self.rotation_matrix(axis, theta))
	def y_rotate(self,theta):
		"""
		one lap is 2π.
		"""
		axis = [0, 1, 1]
		self._atomPos=np.dot(self._atomPos,self.rotation_matrix(axis, theta))

if __name__ == '__main__':
	CuHHTP = Compound('CuHHTP')
	CuHHTP.load_xyz('./new.xyz')
	# CuHHTP.save('test.xyz')
	# CuHHTP.generate_nw('combo1')
	ascorbic_acid= Compound('ascorbic_acid')
	ascorbic_acid.load_xyz('./ascorbic_acid.xyz')
	CuHHTP.add_molecule(ascorbic_acid)
	CuHHTP.translate(1,1,12)
	CuHHTP.save('combo1.xyz')

