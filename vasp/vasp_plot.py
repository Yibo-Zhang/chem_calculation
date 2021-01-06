import matplotlib.pyplot as plt
from pymatgen.io.vasp.outputs import Vasprun
from pymatgen.electronic_structure.plotter import BSDOSPlotter,\
BSPlotter,BSPlotterProjected,DosPlotter

bs_vasprun = Vasprun("./vasprun.xml",parse_projected_eigen=True)
bs_data = bs_vasprun.get_band_structure(line_mode=True)

dos_vasprun=Vasprun("./vasprun.xml")
dos_data=dos_vasprun.complete_dos

banddos_fig = BSDOSPlotter(bs_projection='elements', dos_projection='elements',fig_size=(20, 10))
banddos_fig.get_plot(bs=bs_data, dos=dos_data)
plt.savefig('BSDOS_elements.png',img_format='png')

banddos_fig = BSDOSPlotter(bs_projection='elements', dos_projection='orbitals',fig_size=(15, 10))
banddos_fig.get_plot(bs=bs_data, dos=dos_data)
plt.savefig('BSDOS_orbits.png',img_format='png')

# pband_fig = BSPlotterProjected(bs=bs_data)
# pband_fig = pband_fig.get_projected_plots_dots({'Mn':['d','s']})
# # plt.savefig('pband_orbital_fig.png',img_format='png')
