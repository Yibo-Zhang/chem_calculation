import numpy as np
import matplotlib.pyplot as plt

with open('DOSCAR','r') as f:
    line = f.readline()
    print(line)
    Number_of_Ions = int(line.split()[0])
    if_PDOS = True if int(line.split()[2])==1 else False
    for i in range(4):
        print(f.readline())
    infor_line = f.readline().split()
    NDOS = int(infor_line[2])
    Fermi_Energy = float(infor_line[3])

    print('Fermi_energy: ',Fermi_Energy)
    print('NDOS:         ',NDOS)

    total_DOS = []
    for i in range(NDOS):
        line = f.readline().split()
        line = line[0:2]
        total_DOS.append(line)

    print(f.readline())
    PDOS = []
    pDOS_number = Number_of_Ions*9+1 if if_PDOS else Number_of_Ions*3+1
    for i in range(NDOS):
        line = f.readline().split()
        line = line[0:pDOS_number]
        PDOS.append(line)

    for i in range(10):
        line = f.readline().split()
        print(len(line))

total_DOS = np.array(total_DOS).astype(float)
# 减去 费米能
fermi_dos = np.array([Fermi_Energy,0]*NDOS).reshape(NDOS,2).astype(float)
total_DOS = np.subtract(total_DOS,fermi_dos)



PDOS = np.array(PDOS).astype(float)
# 减去 费米能
fermi_pdos = [Fermi_Energy]
fermi_pdos.extend([0]*(9))
fermi_pdos = np.array(fermi_pdos*NDOS).reshape(NDOS,10).astype(float)
PDOS = np.subtract(PDOS,fermi_pdos)

# show total_DOS
def plot_DOS(total_DOS):
    plt.figure(figsize=(8,4))
    dos_plot = plt.plot(total_DOS[:,0],total_DOS[:,1],label='DOS')
    plt.xlim((-20,20))
    plt.xlabel('E-E(f) ev')
    plt.ylabel('DOS')
    plt.legend()
    plt.savefig('total_DOS.png',dpi=300)

def plot_pDOS_up_down(PDOS):

    label_list = 's  p_y p_z p_x d_{xy} d_{yz} d_{z2-r2} d_{xz} d_{x2-y2}'.split()

    fig, axes = plt.subplots(
        nrows=3, ncols=3, sharex=True, sharey=True, figsize = (12,12)
    )

    for i in range(1,10):
        b = (i-1)%3
        a = (i-1)//3
        ax = axes[a,b]
        ax.plot(PDOS[:,0],PDOS[:,2*i-1],label=label_list[i-1]+'_up')
        ax.plot(PDOS[:,0],PDOS[:,2*i],label=label_list[i-1]+'_down')
        plt.xlim(-20,20)
        plt.ylim(-0.2,0.5)
        ax.legend()
        plt.savefig(label_list[i-1]+'.png',dpi=300)

def plot_pDOS(PDOS):

    label_list = 's  p_y p_z p_x d_{xy} d_{yz} d_{z2-r2} d_{xz} d_{x2-y2}'.split()

    fig, axes = plt.subplots(
        nrows=3, ncols=3, sharex=True, sharey=True, figsize = (12,12)
    )

    for i in range(5,10):
        b = (i-1)%3
        a = (i-1)//3
        ax = axes[a,b]
        ax.plot(PDOS[:,0],PDOS[:,i],label=label_list[i-1])
        plt.xlim(-20,20)
        plt.ylim(0,1.5)
        ax.legend()
        plt.savefig(label_list[i-1]+'_total.png',dpi=300)


plot_DOS(total_DOS)
plot_pDOS_up_down(PDOS)
plot_pDOS(PDOS)
