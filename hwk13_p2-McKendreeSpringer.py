import numpy as np
import matplotlib.pyplot as plt

def isf(x):
    '''importance sampling formula'''
    return (1/(np.exp(x)+1))*2

def p(x):
    return 1/(2*x**0.5)

def w(x):
    return x**-0.5

def int_w(x):
    return -0.5*x**-1.5

if __name__ == "__main__":
    N = 1000000 #number of sample points
    a = 0.000000000001 #start of integral
    b = 1 #end of integral
    
    #plots p(x) and w(x) probability distributuion for comparison
    x = np.linspace(a,b,N)
    plt.plot(x, p(x), label='p(x)')
    plt.plot(x, w(x)/abs(int_w(b)-int_w(a)),color='red', label='w(x) probability function')
    plt.yscale('log')
    plt.legend()
    plt.savefig('plotComparison.png')
    plt.show()

    #integrates via importance sampling
    count = 0
    for i in range(N):
        #draws random xpoint
        x = np.random.random()**2
        xi = isf(x)
        count += xi
    integral = count/N
    print('The value of the integral:',integral)

