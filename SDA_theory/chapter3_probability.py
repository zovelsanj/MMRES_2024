# 3.19 Practice
# Load misophonia data https://alejandro-isglobal.github.io/SDA/data/data_0 .txt
# • Compute the contingency table of absolute frequencies for misophonia diagnosis (Misofonia.dic) and depression (depresion.dic)
# • Compute the contingency table of relative frequencies for misophonia di- agnosis (Misofonia.dic) and depression (depresion.dic)
# • Compare the differences with exercise 2.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import argparse

def contingency_table_as_heatmap(contingency_table):
    plt.figure(figsize=(8,6))
    sns.heatmap(contingency_table, annot=True, fmt=".2g", cmap="Blues")

    plt.title("Contingency Table of Misophonia vs Depression")
    plt.xlabel("Depression Diagnosis")
    plt.ylabel("Misophonia Diagnosis")
    plt.show()

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True, help="path to misophonia data `data_0.txt`")
    args = parser.parse_args()

    data = pd.read_csv(args.data, delimiter='\t')
    contingency_table_absolute = pd.crosstab(data['Misofonia.dic'], data['depresion.dic'], normalize=False)
    contingency_table_relative = pd.crosstab(data['Misofonia.dic'], data['depresion.dic'], normalize=True)

    contingency_table_as_heatmap(contingency_table_relative)
