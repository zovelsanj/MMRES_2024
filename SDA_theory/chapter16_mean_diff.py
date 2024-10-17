import numpy as np
import pandas as pd
from scipy import stats
import argparse

def mean_difference(path, significance=0.05):
    '''PROBLEM: Leptin is an adipose tissue hormone that creates the sensation of satiety after eating. 
    We want to study the serum leptin levels in obese children (PMID: 18755049) under different conditions, such as sex.
    We therefore assume A: female and B: male and are **normally distributed with different mean and variances**. 
    Load data `leptin_sex.txt`.
    If we consider 𝛿, the difference between means 𝛿 = 𝜇𝐴 −𝜇𝐵, then the hypotheses can be written as
    a. H0: 𝛿=0 b. H1: 𝛿≠0`'''

    data = pd.read_csv(path, sep="\t")
    groupA = data[data['sex']=="girl"]['leptin']
    groupB = data[data['sex']=="boy"]['leptin']

    #Estimators
    yA_mean = np.mean(groupA)
    yB_mean = np.mean(groupB)
    s2A = np.var(groupA, ddof=1)
    s2B = np.var(groupB, ddof=1)

    #Hypothesis
    H0 = "𝛿=0"
    H1 = "𝛿≠0" #Since our research interest is 𝛿≠0, we need to look on both sides of the distrubution, so our test will be two-tailed

    #Assuming H0 is true, difference between means
    d = (yA_mean-yB_mean)/np.sqrt(s2A/len(groupA)+s2B/len(groupB))
    p_value= 2*(1-stats.norm.cdf(d)) #two-tailed test, we use nornal distrubution which we can find out by visualizing the data distribution

    print(f"p-value: {p_value}")
    if p_value <= significance: 
        print(f"Reject the Null Hypothesis: {H0}, Accept Alternative Hypothesis: {H1}")
    else:
        print(f"Accept the Null Hypothesis: {H0}")

def mean_difference_mice(path, significance=0.05):
    '''In a study that wanted to test the effect of leptin in neurodevelopment, 7 male mice had their leptin gene knocked out. And, they could not pro- duce the horomone. 
    While 16 mice were left with normal leptin function (PMID:30694175). These are called wild type. 
    An initial question was to test the effect of leptin on the body weight of the animals. 
    Is the mean weight of the animals different between wild types and knock-outs?
    We assume that, both data are **normally distributed with same variance**.
    If we consider 𝛿, the difference between means 𝛿 = 𝜇𝐴 −𝜇𝐵, then the hypotheses can be written as
    a. H0: 𝛿=0 b. H1: 𝛿≠0`
    '''
    data = pd.read_csv(path, sep="\t")
    groupA = data["Control"]
    groupB = data["LepNull"]

    #Hypothesis
    H0 = "𝛿=0"
    H1 = "𝛿≠0" #Since our research interest is 𝛿≠0, we need to look on both sides of the distrubution, so our test will be two-tailed
    statistic = stats.ttest_ind(groupA, groupB, equal_var=True, nan_policy='omit')
    print(f"Statistic: {statistic}")

    p_value = statistic[1]
    if p_value <= significance: 
        print(f"Reject the Null Hypothesis: {H0}, Accept Alternative Hypothesis: {H1}")
    else:
        print(f"Accept the Null Hypothesis: {H0}")

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True, help="path to misophonia data `data_0.txt`")
    args = parser.parse_args()

    # mean_difference(path=args.data)
    mean_difference_mice(path=args.data)
