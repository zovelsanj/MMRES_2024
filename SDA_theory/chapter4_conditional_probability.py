# 4.12 Practice
# Load misophonia data from https://alejandro-isglobal.github.io/SDA/data/da ta_0.txt
# • Compute the conditional probability table of misophophonia (Misofo- nia.dic) given marital status (Estado). What is the estimated probability of having misophonia if the patient is married?
# • Compute the conditional probability table of marital status (Estado) given misophonia (Misofonia.dic). What is the estimated probability of being married if the patient is misophonic?

import argparse
import pandas as pd

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True, help="path to misophonia data `data_0.txt`")
    args = parser.parse_args()

    data = pd.read_csv(args.data, delimiter='\t')