import numpy as np
from scipy.optimize import leastsq
import pylab as pl

x = np.arange(1, 17, 1)
y = np.array([4.00, 6.40, 8.00, 8.80, 9.22, 9.50, 9.70, 9.86, 10.00, 10.20, 10.32, 10.42, 10.50, 10.55, 10.58, 10.60])

# 第1個擬合，自由度為3
z1 = np.polyfit(x, y, 3)
# 生成的多項式對象
p1 = np.poly1d(z1)
print(z1)
print(p1)

# 第2個擬合，自由度為6
z2 = np.polyfit(x, y, 6)
# 生成的多項式對象
p2 = np.poly1d(z2)
print(z2)
print(p2)

# 繪制原曲線及擬合後的曲線

# 原曲線
pl.plot(x, y, 'b^-', label='Origin Line')
# 自由度為3的曲線
pl.plot(x, p1(x), 'gv--', label='Poly Fitting Line(deg=3)')
pl.plot(x, p2(x), 'r*', label='Poly Fitting Line(deg=6)')
pl.axis([0, 18, 0, 18])
pl.legend()
# Save figure
pl.savefig('scipy02.png', dpi=96)