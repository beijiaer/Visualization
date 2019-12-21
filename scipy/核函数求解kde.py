from scipy import stats
import numpy as np
import pylab as pl
x = range(1,7)
p = (1.0/6, 1.0/6, 1.0/6, 1.0/6, 1.0/6, 1.0/6)
dice = stats.rv_discrete(values=(x, p))
samples = dice.rvs(size=(20000,50))
samples_mean = np.mean(samples, axis=1)
_,bins,step = pl.hist(
    samples_mean, bins=100, normed=True, histtype="step", label="Histogram")
kde = stats.kde.gaussian_kde(samples_mean)
x = np.linspace(bins[0],bins[-1],100)
pl.plot(x, kde(x),label="kde")
mean, std = stats.norm.fit(samples_mean)
pl.plot(x, stats.norm(mean,std).pdf(x), alpha=0.8, label="normal fitting")
pl.legend()
pl.show()
