import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline

T = np.array([5, 250, 500, 750, 1000])
power = np.array([0.224, 0.650, 0.720, 0.740, 0.766])
xnew = np.linspace(T.min(),T.max(),100) #300 represents number of points to make between T.min and T.max

T1 = np.array([5, 250, 500, 750, 1000])
power1 = np.array([0.034, 0.380, 0.430, 0.479, 0.536])
xnew1 = np.linspace(T1.min(), T1.max(),100)

power_smooth = spline(T,power,xnew)
plt.plot(xnew,power_smooth)

power_smooth1 = spline(T1,power1,xnew1)
plt.plot(xnew1,power_smooth1)

plt.show()