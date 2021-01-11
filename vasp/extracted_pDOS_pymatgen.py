import matplotlib.pyplot as plt
from pymatgen.io.vasp.outputs import Vasprun
from pymatgen.core import sites
from pymatgen.electronic_structure.core import Orbital,Spin
import numpy as np
import pandas as pd
import os
import errno

if_soc = int(input('SOC is open(1) or not(0): '))
if_soc = True if if_soc==1 else False

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
if if_soc:
    col =['energy']
    col.extend([i+'_'+j for i in pdos_list for j in spin])
    for i in pdos_list:
        for j in spin:
            pdos = np.concatenate((pdos,Cr_pdos[Orbital[i]][Spin[j]].reshape(NDOS,1)),axis=1)
else:
    col =['energy']
    col.extend([i for i in pdos_list ])
    for i in pdos_list:
        pdos = np.concatenate((pdos,Cr_pdos[Orbital[i]][Spin['up']].reshape(NDOS,1)),axis=1)


        
# Cr_pdos_dxy_up = Cr_pdos[Orbital['dxy']][Spin['up']]

# save to file
import pandas as pd
col =['energy']
col.extend([i+'_'+j for i in pdos_list for j in spin])
data_set = pd.DataFrame(pdos,columns=col)
# add pdos 
for i in pdos_list:
    data_set[i] = data_set[i+'_up'] +data_set[i+'_down']
# add total dos
data_set['total'] = sum([data_set[i] for i in pdos_list])
data_set.to_csv("data.csv",index=None)

# save fig

def save_fig(df,pdos_list):    
    try:
        os.makedirs('png')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    for i in range(len(pdos_list)):
        y_lable_1 = pdos_list[i]+'_'+'up'
        ax = df.plot(x='energy',y=y_lable_1,xlim=[-20,20],ylim=[-0.3,0.6],legend=y_lable_1)
        y_lable_2 = pdos_list[i]+'_'+'down'
        df.plot(x='energy',y=y_lable_2,legend=y_lable_2,ax=ax)
        ax.get_figure().savefig('./png/'+pdos_list[i]+'.png',dpi=150)
    
    for i in pdos_list:
        ax = df.plot(x='energy',y=i,xlim=[-20,20],ylim=[-0.3,1.5],legend=i)
        ax.get_figure().savefig('./png/'+i+'_total.png',dpi=150)
    ax = df.plot(x='energy',y='total',xlim=[-20,20],ylim=[-0.3,3],legend='total')
    ax.get_figure().savefig('./png/'+'total.png',dpi=150)
    


save_fig(data_set,pdos_list)
