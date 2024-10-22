import numpy as np
import matplotlib.pyplot as plt

def gaussian_2d(x1, x2, mu1=0, mu2=10, rho=0.8, s1=1, s2=1):
    """returns a 2D gaussian. Try changing the values"""
    return np.exp(-0.5/(1-rho**2) * ((x1-mu1)**2/s1**2 + (x2-mu2)**2/s2**2 - 2*rho*(x1-mu1)*(x2-mu2)/s1/s2))
    
def plot_gaussain(mu1=0, mu2=10, s1=1, s2=1):
    """rho: correlation coeffecient"""
    x1_min, x1_max = mu1-2*s1, mu1+2*s1
    x2_min, x2_max = mu2-2*s2, mu2+2*s2
    x1, x2 = np.meshgrid(np.arange(x1_min,x1_max, 0.01), np.arange(x2_min,x2_max, 0.01))
    gauss =  gaussian_2d(x1, x2)

    plt.figure(figsize=(10,5))
    plt.imshow(gauss,extent=[x1_min,x1_max,x2_min,x2_max], origin='lower', alpha=0.8, aspect='auto')
    plt.colorbar()
    plt.xlabel(r'$x_1$')
    plt.ylabel(r'$x_2$')
    plt.title(r'2D Gaussian')
    plt.show()

def proposal(d1, d2, prop_width=0.5, s1=1, s2=1):
    """try chanigng the proposal width"""                
    p1 = np.random.normal(d1, prop_width*s1)
    p2 = np.random.normal(d2, prop_width*s2)
    return p1, p2

def plot_markov_chain(chain, burnin_period=10, remove_burnin=True):
    if remove_burnin:
        chain = chain[burnin_period:]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))

    # Visualize each dimension of the chain
    ax1.plot(chain[:,1], color='lightskyblue', lw=2, alpha=0.9, label=r'$x_2$')
    ax1.plot(chain[:,0], color='darkslategrey', lw=2, alpha=0.7, label=r'$x_1$')
    ax1.set_xlabel(r'Chain step')
    ax1.axvspan(0, burnin_period, color='tomato', alpha=0.1, label='Burn-in')
    ax1.legend(frameon=True)
    ax1.set_xscale('log')
    ax1.set_title('Markov Chain Progression')

    # Visualize chain as Gaussian
    ax2.scatter(chain[:,0], chain[:, 1], s=0.1, color='darkslategrey', alpha=0.7)
    ax2.set_xlabel(r'$x_1$')
    ax2.set_ylabel(r'$x_2$')
    ax2.set_title(r'Sampling of 2D Gaussian')

    plt.tight_layout()
    plt.show()

def metropolis_hasting(Nsim=10**5, plot=True):
    """sampling probability distrbution using Metropolis Hasting Monte Carlo"""
    chain = np.zeros((Nsim, 3))            # Initialize the chain, including pdf
    x1_0, x2_0 = 0., 12.                  # We can play with this
    chain[0] = x1_0, x2_0, gaussian_2d(x1_0, x2_0, rho=0.99)
    count_accepted = 0                   # This is to keep track of how many accepted proposals we have

    for i in range(Nsim-1):                         # Fill the chain with MH sampling
        x_prop1, x_prop2 = proposal(chain[i,0], chain[i,1], prop_width=0.5)
        pdf_prop = gaussian_2d(x_prop1, x_prop2, rho=0.99)
        ratio =  pdf_prop / chain[i,2]

        if ratio >= 1 or ratio > np.random.random():
            chain[i+1] = x_prop1, x_prop2, pdf_prop
            count_accepted += 1

        else:
            chain[i+1] = chain[i]

    if plot:
        plot_markov_chain(chain)   
    print(f"chain efficiency: {count_accepted/Nsim}") 
    # Do we recover the input parameters of our 2dGaussian?
    print(f"x1 mean: {chain[:, 0].mean()}, x2 mean: {chain[:,1].mean()}")               
    print(f"x1 sd: {chain[:, 0].std(ddof=1)}, x2 sd: {chain[:,1].std(ddof=1)}") 
    print(f"correlation coeff: {np.corrcoef(chain[:, 0], chain[:,1])[0,1]}")


if __name__=="__main__":
    metropolis_hasting()
    