import numpy as np
from scipy.stats import chi2_contingency

def proportions_two_hospitals():
    '''PROBLEM: We perform diagnostic surveillance in both hospitals and found
    • Hospital Aincluded in the study a total of nA= 200 and observed 18 infections.
    • Hospital B included in the study a total of nB = 400 and observed 46 infections.'''
    #create 2x2 contingency table
    observed = np.array([[182, 18], [354, 46]])

    chi2, p, dof, expected = chi2_contingency(observed, correction=False)
    print(f"chi-squared statistic: {chi2}, p-value: {p}")


def proportions_several():
    '''PROBLEM: Now, we want to know if the frequency of hepatitis C is different across 5 difference hospitals.
    We then formulate the hypothesis contrast: a. H0 :p=pA=pB =pC =pD =pE
    The null hypothesis (status quo) assumes that hospital (i = {A,B,C,D,E}) and disease (j = {yes,no}) are all independent and then they have the same infection rate.
    b. H1 : p ≠ p(A U B U C U D U E)'''
    # Create the 2x5 contingency table     
    observed = np.array([[18, 46, 25, 15, 10], [182, 354, 375, 85, 90]])

    chi2, p_value, dof, expected = chi2_contingency(observed, correction=False)
    print(f"chi-squared statistic: {chi2}, p-value: {p_value}")
