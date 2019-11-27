import re
import sys
import os

def get_inputs():
    if (not len(sys.argv) == 2):
        print('Usage: get_all_xyz.py OUTPUT_file\n')
        print('  OUTPUT_FILE: Optimized output file from nwchem\n')
        sys.exit()
    else:
        xyz_file_name = sys.argv[1]
        return xyz_file_name


class Output(object):
    def __init__(self):
        super(Output, self).__init__()

    ####### get optimized structure
    def load_nwoutput(self, dir):
        self.dir = dir
        self.structure = []
        self.begin_number = 0
        self.end_number = 0
        # pattern = re.compile(r'Output coordinates in angstroms')
        start_pattern = re.compile(r'Output')
        end_pattern = re.compile(r'Atomic Mass')
        start_num = 0
        end_num = 0
        locker = False
        with open(dir, 'r') as nwoutput:
            lines = nwoutput.readlines()
            for n, i in enumerate(lines):
                start_match = re.search(start_pattern, i)
                if start_match:
                    start_num = n
                    self.begin_number += 1
                    locker = True
                end_match = re.search(end_pattern, i)
                if end_match:
                    end_num = n
                    self.end_number += 1
                if self.begin_number and self.end_number and self.begin_number == self.end_number and locker:
                    locker = False
                    start_num += 4
                    end_num -= 1
                    self.structure = lines[start_num:end_num]
                    self.save_trajectory(self.begin_number)

    def save_trajectory(self, number):
        structure = ''
        length = len(self.structure)
        structure = structure + str(length) + '\n\n'
        for i in self.structure:
            words = i.split()
            structure = structure + words[1] + ' ' * 4
            structure = structure + words[3] + ' ' * 4
            structure = structure + words[4] + ' ' * 4
            structure = structure + words[5] + ' ' * 4
            structure = structure + '\n'
        dir_list = self.dir.split('/')
        dir_list = dir_list[:-1]
        new_dir = '/'.join(dir_list) + '/xyz'
        name = 'xyz'
        print(new_dir)
        # check if new_dir exist 
        if not os.path.exists(new_dir):
            os.mkdir(new_dir)
            print("Directory " , new_dir ,  " Created ")
        else:
            print("Directory " , new_dir ,  " already exists")
        destination = os.path.join(new_dir,name+'_'+str(number)+'.xyz')
        print(destination)
        with open(destination, 'w') as f:
            f.write(structure)


if __name__ == '__main__':
    out = Output()
    input_file = get_inputs()
    out.load_nwoutput(input_file)
