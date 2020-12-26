from scipy import signal
from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline


angle = np.linspace(-np.pi, np.pi, 50)
cirx = np.sin(angle)
ciry = np.cos(angle)
a = [1/13, 1/13, 1/13, 1/13, 1/13, 1/13, 1/13,
     1/13, 1/13, 1/13, 1/13, 1/13, 1/13]
H = np.roots(a)
b = [1, 0, 0, 0]
z = np.roots(b)

plt.figure(figsize=(8, 8))
plt.plot(cirx, ciry, 'k-')
plt.plot(np.real(H), np.imag(H), 'o', markersize=12)

plt.plot(np.real(z), np.imag(z), 'x', markersize=12)
plt.grid()

plt.xlim((-2, 2))
plt.xlabel('Real')
plt.ylim((-2, 2))
plt.ylabel('Imag')
