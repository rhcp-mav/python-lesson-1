import numpy as np
import matplotlib.pyplot as plt


def main():
    x = np.arange(-10, 10.01, 0.01)
    #plt.plot(x, np.sin(x), x, np.cos(x), x, -x)
    plt.plot(x, x**2, x, x**3, x, x**4, scalex=True, scaley=True)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$f(x)$')
    plt.title(r'$f_1(x)=\sin(x),\ f_2(x)=\cos(x),\ f_3(x)=-x,\  f_4(x)=x**2$')
    plt.grid(True)
    plt.show()


main()
