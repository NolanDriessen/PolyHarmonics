
from pylab import *
import scipy.signal as signal
#A function to plot frequency and phase response
def mfreqz(b,a=1):
    w,h = signal.freqz(b,a)
    h = abs(h)
    return(w/max(w), h)

n = 11.
n
b = repeat(1/n, n)
b

w, h = mfreqz(b)
#Plot the function
plot(w,h,'k')
ylabel('Amplitude')
xlabel(r'Normalized Frequency (x$\pi$rad/sample)')
show()

print 
for i in range(10):
    print(" " , round(h[i],2) , "," , round(w[i],2))