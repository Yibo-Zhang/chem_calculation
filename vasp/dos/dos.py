import numpy as np
import matplotlib as mpl
mpl.use('Agg') #silent mode
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker

#------------------ FONT_setup ----------------------
font = {'family' : 'arial', 
    'color'  : 'black',
    'weight' : 'normal',
    'size' : 13.0,
    }

#------------------- Data Read ----------------------
with open("PDOS_Cr_SOC.dat","r") as reader:
	legend = reader.readline()
legends=legend.split()[1:]
legends=[i.replace("_"," ") for i in legends]
legend_s=tuple(legends)
datas=np.loadtxt("PDOS_Cr_SOC.dat",dtype=np.float64,skiprows=1)

#--------------------- PLOTs ------------------------
axe = plt.subplot(111)
# Color methods! choose only one of the two methods
axe.plot(datas[:,0],datas[:,1:],linewidth=1.0) #auto colors

axe.set_xlabel(r'${E}$-$E_{f}$ (eV)',fontdict=font)
axe.set_ylabel(r'PDOS (states/eV)',fontdict=font)
plt.yticks(fontsize=font['size']-2,fontname=font['family'])
plt.legend(legend_s,loc='best')
plt.xlim(( -40,  110)) # set y limits manually
plt.ylim(0,2) # set y limits manually
leg = plt.gca().get_legend()
ltext = leg.get_texts()
plt.setp(ltext, fontsize=font['size']) 
fig = plt.gcf()
fig.set_size_inches( 8, 6)
plt.savefig('dos.png',dpi= 300)
