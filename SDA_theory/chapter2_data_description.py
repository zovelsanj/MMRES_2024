# 2.26 Practice
# Load misophonia data from https://alejandro-isglobal.github.io/SDA/data/da ta_0.txt
# 1. Extract misophonia variable (Misofonia.dic) 
#     • Doabarplotandapiechart
# 2. Extract convexity angle variable (Angulo_convexidad)
#     • Calculate its sample mean (average), standard deviation and make a his- togram
#     • Calculate its median and inter-quartile range
#     • Draw a boxplot

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import argparse

def read_data(path, column_name):
    data = pd.read_csv(path, delimiter='\t')
    return data[column_name]

def plots(data, type="bar"):
    data_series = data.value_counts()
    data_idxs = data_series.index
    frequency = data_series.values

    if type=="bar":
        plt.bar(data_idxs, frequency)
        plt.xlabel("data")
        plt.ylabel("frequency")
        plt.title("Misofonia.dic Bar Plot")
    elif type=="pie_chart":
        plt.pie(frequency, labels=data_idxs)
        plt.title("Misofonia.dic Pie Chart")

    else:
        raise Exception("Pass `bar` for bar plot and `pie_chart` for pie chart")
    plt.show()

def get_stats(data, plot=""):
    data_stats = {}
    data_stats["mean"] = np.mean(data)
    data_stats["sd"] = np.std(data)
    data_stats["median"] = np.median(data)
    Q1 = np.percentile(data, 25)
    Q3 = np.percentile(data, 75)
    data_stats["iqr"] = Q3-Q1

    if plot=="hist":
        plt.hist(data, bins=10)
        plt.xlabel("data")
        plt.ylabel("frequency")
        plt.title("Angulo_convexidad Histogram")
        plt.show()
    
    elif plot=="box":
        fig, ax = plt.subplots()
        ax.boxplot(data)
        ax.annotate(f'Mean: {data_stats["mean"]:.2f}', xy=(1,  data_stats["mean"]), xytext=(1.1,  data_stats["mean"]),
            arrowprops=dict(facecolor='black', arrowstyle='->'), verticalalignment='center')
        
        ax.annotate(f'Median: {data_stats["median"]:.2f}', xy=(1, data_stats["median"]), xytext=(1.1, data_stats["median"]),
            arrowprops=dict(facecolor='blue', arrowstyle='->'), verticalalignment='center')
        
        ax.annotate(f'Q1: {Q1:.2f}', xy=(1, Q1), xytext=(1.1, Q1), arrowprops=dict(facecolor='green', arrowstyle='->'),
            verticalalignment='center')
        
        ax.annotate(f'Q3: {Q3:.2f}', xy=(1, Q3), xytext=(1.1, Q3), arrowprops=dict(facecolor='red', arrowstyle='->'),
            verticalalignment='center')
        
        ax.set_title("Angulo_convexidad Box Plot")
        plt.show()
    return data_stats

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True, help="path to misophonia data `data_0.txt`")
    args = parser.parse_args()

    misofonia_data = read_data(args.data, column_name="Misofonia.dic")
    angulo_convexidad_data = read_data(args.data, column_name="Angulo_convexidad")

    #Practice Question 1
    plots(misofonia_data, type="pie_chart") 
    #Practice Question 2
    stats = get_stats(angulo_convexidad_data, plot="box")
    print(f'Mean = {stats["mean"]}, Median = {stats["median"]}, SD = {stats["sd"]}, IQR = {stats["iqr"]}')
