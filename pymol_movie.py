'''
Uses pymol to generate images for a movie showing real-time electronic dynamics

Copyright (C) 2017  Patrick J Lestrange
Modified by Craig T. Chapman

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import sys
import os
import pymol


xyzprefix = "test"
pymol.finish_launching()
# start numbering for the frames (not the same as the cubes)
file_num = 1

# define the starting and ending indices for the cube files
istart, iend = 1,4

# create a directory to store the new fchk/cube files
frames_dir = '/Users/yibo/Desktop/trajectory/xyz/frames'
if not os.path.exists(frames_dir):
    os.makedirs(frames_dir)

# Loop over the frames for each step to be rendered
for i in range(istart,iend):
    # clear the frame
    pymol.cmd.reinitialize()
    xyz_name = xyzprefix+'_'+str(file_num+1)+'.xyz'
    pymol.cmd.load(xyz_name, 'xyz')
    pymol.cmd.show('sticks', 'xyz')
    pymol.cmd.show('spheres', 'xyz')
    pymol.cmd.set('stick_radius',0.1,'xyz')
    pymol.cmd.set('sphere_scale',0.2)

    pymol.cmd.color('gray','name C*')

    # # plot the density difference
    # cube_file = cubeprefix+'.'+str(file_num+1).zfill(10)+'.cube'
    # pymol.cmd.load(cube_file, 'cube' )
    # pymol.cmd.isosurface('surf1', 'cube',  iso_val)
    # pymol.cmd.isosurface('surf2', 'cube', -iso_val)
    # pymol.cmd.color('density', 'surf1')
    # pymol.cmd.color('gray','surf2')
    # pymol.cmd.set('transparency', 0.2, 'surf1')
    # pymol.cmd.set('transparency', 0.2, 'surf2')

    # reset the camera
    # Note: this needs to be determined for each system individually through
    #       trial and error
    pymol.cmd.zoom()
    #pymol.cmd.turn('x',30)
    pymol.cmd.turn('x',-50)
    # pymol.cmd.zoom('center', 6)
    #pymol.cmd.turn('y',35)
    #pymol.cmd.turn('z',20)
    #pymol.cmd.turn('x',20)
    pymol.cmd.move('z',-0.5)

    # save the frame
    out_file = '%s/frame-%04d' % (frames_dir,file_num)
    # pymol.cmd.set("bg_gradient","on")
    #pymol.cmd.set("bg_rgb_top","[0,0,.1]")
    #pymol.cmd.bg_color(color="palecyan")
    pymol.cmd.set('volume_layers',2000)
    # pymol.cmd.draw(1600,400)
    #pnghack(out_file)
    pymol.cmd.png(out_file,dpi=400.0)

    file_num += 1
