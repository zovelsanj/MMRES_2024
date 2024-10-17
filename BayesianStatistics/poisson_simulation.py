import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, poisson

def plot_hist(priors, nbin=50, Nobs=3):
    fig = plt.figure(figsize=(6,4))
    n, bins, patches = plt.hist(priors[0], nbin, density=True, color='cornflowerblue',alpha=0.5, label='Uniform prior')
    plt.gca().hist(priors[1], nbin, density=True, color='tomato',alpha=0.5, label='Jeffreys prior')
    plt.gca().legend(frameon=False)
    plt.plot(bins, poisson.pmf(Nobs, bins), linewidth=2, color='darkslategrey', alpha=0.7, label='Analytical posterior, uniform prior')
    mu, sigma = priors[0].mean(), priors[0].std(ddof=1)          # Overlay a Gaussian with mu = <lambda> and var = Var(lambda) (sample var, so ddof=1)
    plt.gca().plot(bins, norm.pdf(bins, mu, sigma), linewidth=2, ls='dashed', color='darkolivegreen', label='Gaussian approximation')
    plt.gca().legend(frameon=False)

    plt.xlabel(r'$\lambda$')
    plt.ylabel(r'$p(\lambda)$')
    plt.show()

def get_poisson_prior(Nobs=3, Nsim=10**7):
    #Flat prior
    lmax = max(10, Nobs + 10*np.sqrt(Nobs)) # Maximum for flat prior on lambda (this would be infinity, but we need a finite, large number)
    prior_flat = np.random.random(Nsim) * lmax
    n_flat = np.random.poisson(prior_flat)
    posterior_flat = prior_flat[n_flat == Nobs] # Keep the lambda's for which n = Nobs

    #Jeffreys prior
    prior_jeffreys = lmax**(2*np.random.random(Nsim)-1)
    n_jeffreys = np.random.poisson(prior_jeffreys)
    posterior_jeffreys = prior_jeffreys[n_jeffreys == Nobs] # Keep the lambda's for which n = Nobs

    return posterior_flat, posterior_jeffreys

def poisson_simulation(Nobs=3, Nsim=10**7):
    posterior_flat, posterior_jeffreys = get_poisson_prior(Nobs, Nsim)
    plot_hist(priors=[posterior_flat, posterior_jeffreys])

if __name__=="__main__":
    poisson_simulation(Nobs=3, Nsim=10**5)