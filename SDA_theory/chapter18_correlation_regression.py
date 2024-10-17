import argparse
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from scipy.stats import pearsonr
from statsmodels.formula.api import ols

def correlation(data, vars:list):
    leptin = data[vars[0]]
    fatmass = data[vars[1]]
    correlation = pearsonr(leptin, fatmass)
    print(f"correlation coefficient: {correlation[0].round(3)}, p-value: {correlation[1].round(4)}")

    plot_correlation(vars, correlation[0])
    return correlation

def plot_ellipse(ax, xdata, ydata, pearson_corr, n_std=1.0, **kwargs):
    """
    Plots an ellipse that covers the data with a given number of standard deviations.
    """
    cov = np.cov(xdata, ydata)  # Covariance matrix
    pearson_corr = cov[0, 1] / (np.sqrt(cov[0, 0]) * np.sqrt(cov[1, 1]))  # Pearson correlation

    ellipse_radius_x = np.sqrt(1 + pearson_corr)
    ellipse_radius_y = np.sqrt(1 - pearson_corr)

    scale_x = np.std(xdata) * n_std
    scale_y = np.std(ydata) * n_std

    mean_x = np.mean(xdata)
    mean_y = np.mean(ydata)

    angle = np.rad2deg(np.arctan2(2 * cov[0, 1], (cov[0, 0] - cov[1, 1])) / 2)

    ellipse = Ellipse((mean_x, mean_y), width=2 * scale_x * ellipse_radius_x, height=2 * scale_y * ellipse_radius_y, angle=angle, **kwargs)
    ax.add_patch(ellipse)

def plot_correlation(vars:list, corr):
    leptin = data[vars[0]]
    fatmass = data[vars[1]]

    sns.set_theme(style="white")

    g = sns.jointplot(x=fatmass, y=leptin, kind="scatter", color="blue", marginal_kws=dict(bins=20, fill=True))
    g.ax_joint.text(0.05, 0.95, f'r = {corr:.2f}', ha='left', va='center', transform=g.ax_joint.transAxes)

    sns.kdeplot(data=fatmass, ax=g.ax_marg_x, color='black')
    sns.kdeplot(data=leptin, ax=g.ax_marg_y, color='black', vertical=True)

    for n_std in range(1, 4):
        plot_ellipse(g.ax_joint, fatmass, leptin, pearson_corr=corr, n_std=n_std, edgecolor='red', facecolor='none', linestyle='-', linewidth=1)

    plt.show()

def linear_regression(data, X, Y):
    ''' mu = alpha + beta*X +eps,
    regression with Ordinary Least Square (OLS) fit'''
    model = ols(f'{Y} ~ {X}', data=data).fit()
    print(model.summary())
    print(model.params)
    plt.scatter(data[X], data[Y])
    plt.plot(data[X], data[X]*model.params["fatmass"]+model.params["Intercept"], color="red")

    plt.xlabel(X)
    plt.ylabel(Y)
    plt.show()

def mulitple_regression(data, X, Y, Z):
    '''mu = alpha + beta*X + gamma*Z + eps'''
    model = ols(f"{Y}~{X}+{Z}", data=data).fit() 
    model_interacton = ols(f"{Y}~{X}*{Z}", data=data).fit() 
    print(model.summary())
    print(model_interacton.summary())
    
    male_data = data[data[Z]=="M"]
    female_data = data[data[Z]=="F"]

    plt.scatter(male_data[X], male_data[Y])
    plt.scatter(female_data[X], female_data[Y])
    
    plt.plot(data[X], data[X]*model.params["fatmass"]+model.params["Intercept"], color="red") # mu_F=a;pha+(beta+eps)*X
    plt.plot(data[X], data[X]*model.params["fatmass"]+model.params["Intercept"]+model.params["sex[T.M]"], color="green") #mu_M=(alpha+gamma)+(beta+eps)*X

    plt.xlabel(X)
    plt.ylabel(Y)
    plt.show()

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True, help="path to misophonia data `leptinFatmass.txt`")
    parser.add_argument("--stat", required=False, help="corr, lin_reg, mul_reg`")
    args = parser.parse_args()

    data = pd.read_csv(args.data, sep="\t")
    print(data.head(5))

    if args.stat=="corr":
        corr = correlation(data, vars=["leptin", "fatmass"])
    elif args.stat=="lin_reg":
        linear_regression(data, X="fatmass", Y="leptin")
    elif args.stat=="mul_reg":
        mulitple_regression(data, X="fatmass", Y="leptin", Z="sex")
