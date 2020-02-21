pymol.cmd.load(xyz_name, 'xyz')
pymol.cmd.show('sticks', 'xyz')
pymol.cmd.show('spheres', 'xyz')
# set valence,0
pymol.cmd.set('stick_radius',0.1,'xyz')
pymol.cmd.set('sphere_scale',0.2)
pymol.cmd.color('gray50','all')
pymol.util.cnc("all")
as sticks
set stick_h_scale, 1,
set valence,0

set sphere_scale, 0.8, mof, 
set stick_radius, 0.2,mof


set stick_radius, 0.2, other,
set sphere_transparency, 0.6
set dash_radius, 0.0800