import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
num=[1]
denom=[1,2,1]
t_f=signal.TransferFunction(num,denom)
omega=np.logspace(-2,2,1000)
_,mag,phase=signal.bode(t_f,omega)
plt.subplot(2,1,1)
plt.semilogx(omega,mag)
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.title("Magnitude Plot")
plt.subplot(2,1,2)
plt.semilogx(omega,phase)
plt.xlabel("Frequency")
plt.ylabel("Phase")
plt.title("Phase Plot")
plt.tight_layout()
plt.show()