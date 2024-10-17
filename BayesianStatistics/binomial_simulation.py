import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

def plot_hist(theta, nbins=50, label="Simulated", Ntrials=100, Nobs=0):
    fig = plt.figure(figsize=(5, 5))
    n, bins, patches = plt.hist(theta, nbins, density=True, color='cornflowerblue',alpha=0.5, label=label)
    plt.gca().plot(bins, (Ntrials+1) * binom.pmf(Nobs, Ntrials, bins), linewidth=3, color='darkslategrey',alpha=0.8, label='Analytical')

    mu, sigma = theta.mean(), theta.std(ddof=1)             # Overlay a Gaussian with mu=<p> and var=Var(p) (sample var, so ddof=1)
    plt.gca().plot(bins, norm.pdf(bins, mu, sigma), linewidth=2, ls='dashed', color='tomato', alpha=0.9, zorder=4, label='Gaussian')
    plt.gca().legend(frameon=False)

    plt.xlabel(r"$\theta$")
    plt.ylabel(r"$p(\theta | n, N)$")
    plt.show()

def get_prior(Ntrials, Nobs, Nsim=10**7, prior="uniform"):
    theta = np.random.random(Nsim)
    if prior=="gaussian":
        theta = np.clip(np.random.normal(0.5, 0.1, Nsim), 0 ,1)  # Sample theta uniformly between 0 and 1, NS times (this is our uniform prior)
    
    n = np.random.binomial(Ntrials, theta)
    theta = theta[n==Nobs]
    return theta

def simulate_binomial(Ntrials, Nobs, prior="uniform"):
    """Given a binomial experiment, with N trials and n successes, we want to find the posterior of the parameter 𝜃, 
    the probability of success associated with each binomial experiment: p(𝜃|n,N)."""
    theta = get_prior(Ntrials=Ntrials, Nobs=Nobs, prior=prior)
    plot_hist(theta, Ntrials=Ntrials, Nobs=Nobs)

if __name__=="__main__":
    simulate_binomial(Ntrials=100, Nobs=90, prior="gaussian")
    #NOTE: Always try with different PRIORS. It is always to good to be dominated by data: Even if prioirs are unfair a good quality of data can
    # genereate a fair conclusion. However, the choice of prioir will always affect the posterior (although the conclusion isn't affected much).
    # A biased prioir will generate a biased posterior.
    #This is not important for large N: with a large data set, the choice of non-informative prior does not matter, as we would expect, since the data should dominate the inference. 
    # For small samples, however, the constraining power of the data is not as strong and the choice of prior does matter.