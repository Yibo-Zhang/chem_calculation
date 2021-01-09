import matplotlib.pyplot as plt
from pymatgen.io.vasp.outputs import Vasprun
from pymatgen.core import sites
from pymatgen.electronic_structure.core import Orbital,Spin

import numpy as np

vasprun = Vasprun("vasprun.xml")
dos_data = vasprun.complete_dos
structure = vasprun.structures

fermi_eneregy = dos_data.as_dict()['efermi']
energy_list = dos_data.as_dict()['energies']
NDOS = len(energy_list)
#减去 费米能
energy_list = np.array(energy_list).reshape(NDOS,1) - fermi_eneregy
pdos_list = 's py pz px dxy dyz dz2 dxz dx2'.split()
spin = ['up','down']
Cr_pdos = dos_data.pdos[structure[0][0]]
pdos = energy_list
for i in pdos_list:
    for j in spin:
#         print(Cr_pdos[Orbital[i]][Spin[j]].shape)
        pdos = np.concatenate((pdos,Cr_pdos[Orbital[i]][Spin[j]].reshape(NDOS,1)),axis=1)
        
# Cr_pdos_dxy_up = Cr_pdos[Orbital['dxy']][Spin['up']]

# save to file
import pandas as pd
col =['energy']
col.extend([i+'_'+j for i in pdos_list for j in spin])
data_set = pd.DataFrame(pdos,columns=col)
data_set.to_csv("data.csv",index=None)