import numpy as np
import matplotlib.pyplot as plt

def p(x, x0, gamma):
    '''Probability Density Function
    x0 = mean of distribution
    y = gamma
    '''
    return 1/(np.pi*gamma*(1+((x-x0)/gamma)**2))

def random_cauchy(N,x0,gamma):
    '''N = number of samples
    x0 = mean of distribution
    y = gamma'''
    yList = []
    for i in range(N):
        x = np.random.random()
        y = (1/np.pi*np.arctan((x-x0)/gamma)+1/2)**-1
        yList.append(y)
    return yList

if __name__ == "__main__":
    xVals = np.arange(-20,20,0.1)
    x0 = 0 #mean of distribution
    gamma = 2 #gamma
    N = 10000

    yList = random_cauchy(N, x0, gamma)

    #plots random_cauchy and pdf
    plt.hist(yList, bins=xVals, alpha=0.5, label='random_cauchy function')
    plt.plot(xVals/N,p(x=xVals,x0=x0,gamma=gamma), label='Probability Density Function')
    plt.legend()
    plt.savefig('random_cauchy_and_pdf.png')
    plt.show()
