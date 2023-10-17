import numpy as np
import matplotlib.pyplot as plt
import control as ctl
num=[1]
den=[1,0.5,2]
g=ctl.tf(num,den)
print(g)
ctl.rlocus(g,plot=True)
plt.title("Root Locus Plot")
plt.show()