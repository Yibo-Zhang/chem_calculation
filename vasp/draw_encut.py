import matplotlib.pyplot as plt
import numpy as np
x, y = np.loadtxt('encut.dat', delimiter=' ', unpack=True)
plt.plot(x,y, label='Loaded from file!')

plt.xlabel('Encut')
plt.ylabel('Energy')
#plt.ylim((-23.2,-23))

plt.savefig('encut.png')
