import scipy.signal as sp
import numpy as np
import matplotlib.pyplot as plt

from zplane import zplane
from freqz import freqz

fs = 44.1
fc = 0.15 * np.pi
N = 6
F = [0, 0.15 / 2, 0.15 / 2 + 0.05, 0.5]
A = [1, 0]
W = [1, 100]
filt = sp.remez(N, F, A, W)

plt.plot(filt)
plt.xlabel('Samples')
plt.ylabel('Value')
plt.title('Impulse response: Unwarped version of Filter Coefficients')
plt.show()

freqz(filt)

# warping allpass coefficient:
a = 1.0674 * (2 / np.pi * np.arctan(0.6583 * fs)) ** 0.5 - 0.1916

# warped cutoff frequency
from methods import *

fcw = -warpingphase(fc, a)
print
'fcw', fcw
# normalizing to nyquist
fcny = fcw / np.pi
print
'fcny', fcny
# design filter using remez
Fw = [0, fcny / 2., fcny / 2. + 0.09, 0.5]
wfilt = sp.remez(N, Fw, A, W)

freqz(wfilt)

# Warping Allpass filters:
B = [a.conjugate(), 1]
A = [1, -a]

Imp = np.zeros(80)
Imp[0] = 1
x = Imp

# Y1(z)=A(z), Y2(z)=A^2(z),...
# warped delays
y1 = sp.lfilter(B, A, x)
y2 = sp.lfilter(B, A, y1)
y3 = sp.lfilter(B, A, y2)
y4 = sp.lfilter(B, A, y3)
y5 = sp.lfilter(B, A, y4)

yout = wfilt[0] * x + wfilt[1] * y1 + wfilt[2] * y2 + wfilt[3] * y3 + wfilt[4] * y4 + wfilt[5] * y5

# frequency response
freqz(yout)

# Impulse response
plt.plot(yout)
plt.xlabel('Samples')
plt.ylabel('Value')
plt.title('Impulse response: Warped version of Filter Coefficients')
plt.show()

# zplane(np.roots(yout), 0, [-1.1, 2.1, -1.1, 1.1])
zplane(1. / a.conjugate(), a, [-1.1, 2.1, -1.1, 1.1])



