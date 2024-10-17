#19.3 Group Work session 1: Data description
# When reporting the results of a study, we first describe the variables of interest in tables and figures.
# • We describe demographics (sex, age, marital status, etc..)
# • We describe outcome variables (misophonia)
# • We describe explanatory variables (cephalometric measures, anxiety, depression)
# Imagine we want to study the anxiety of participants in the misophonia study,
# We load the data,
# 1. We describe the participants’ sex, age, and marital status
# b. Age, mean and standard deviation
# c. Age by sex, mean and standard deviation for males, and mean and stan- dard deviation for females
# 2. We describe the clinical outcome, for example, anxiety.

import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def get_stats(data):
    mean = np.mean(data)
    sd = np.std(data)
    return mean, sd

def group_data(data: pd.DataFrame):
    male_age = data[data["Sexo"]=="M"]["Edad"]
    female_age = data[data["Sexo"]=="H"]["Edad"]
    mean_age_male, sd_age_male = get_stats(male_age)
    print(f"mean_age_male: {mean_age_male}, sd_age_male: {sd_age_male}")
    mean_age_female, sd_age_female = get_stats(female_age)
    print(f"mean_age_female: {mean_age_female}, sd_age_female: {sd_age_female}")

def box_plot_by_column(data, x_column, y_column):
    sns.boxplot(data, x=x_column, y=y_column)
    plt.title(f"{x_column} Box Plot by {y_column}")
    plt.show()

def pichart(data:pd.DataFrame, column:str):
    data[column].value_counts().plot(kind="pie")
    plt.title(f"{column} Pie Chart")
    plt.show()
    
def relationship_plot(data, x_column, y_column):
    plt.scatter(data[x_column], data[y_column])
    plt.title(f"Relationship between {x_column} and {y_column}")
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.show()

def describe_dataset(data, viz=False):
    sex = data["Sexo"]
    age = data["Edad"]
    marital_status = data["Estado"]
    anxiety = data["ansiedad.rasgo"]
    anxiety_state = data["ansiedad.estado"]
    anxiety_diagnosed = data["ansiedad.medicada"]
    anxiety_excess = data["ansiedad.dif"]

    print(f"sex: {sex.describe()} \nage: {age.describe()} \nmarital_status: {marital_status.describe()}, \nanxiety: {anxiety.describe()}")
    
    if viz:
        fig, ax = plt.subplots(4, 2, figsize=(10, 8))
        sex.value_counts(sort=False).plot(kind="bar", ax=ax[0][0], rot=0)
        ax[0][0].set_title('Sex Distribution')

        age.plot(kind="hist", ax=ax[0][1], rot=0, edgecolor='black', color="white")
        ax[0][1].set_title('Age Distribution')

        age.plot(kind="box", ax=ax[1][0], rot=0)
        ax[1][0].set_title('Age Box Plot')

        marital_status.value_counts(sort=False).plot(kind="hist", ax=ax[1][1], rot=0)
        ax[1][1].set_title('Marital Status Distribution')
        
        anxiety.plot(kind="hist", ax=ax[2][0], rot=0, edgecolor='black', color="white")
        ax[2][0].set_title('Anxiety Status Distribution')

        anxiety.plot(kind="box", ax=ax[2][1], rot=0)
        ax[2][1].set_title('Anxiety Box Plot')

        anxiety_state.plot(kind="hist", ax=ax[3][0], rot=0, edgecolor='black', color="white")
        ax[3][0].set_title('Anxiety State Status Distribution')

        anxiety_diagnosed.value_counts().plot(kind="bar", ax=ax[3][1], rot=0, edgecolor='black')
        ax[3][1].set_title('Anxiety Diagnosed Distribution')

        plt.tight_layout()
        plt.show()

    mean_age, sd_age = get_stats(age)
    print(f"mean_age: {mean_age}, sd_age: {sd_age}")


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True, help="path to misophonia data `data_0.txt`")
    args = parser.parse_args()

    data = pd.read_csv(args.data, delimiter='\t')
    ## Describe dataset
    # describe_dataset(data, viz=True)

    ## Group dataset
    # group_data(data)

    ## Boxplot based on column (Age by Sex)
    # box_plot_by_column(data, x_column="Sexo", y_column="Edad")

    ## Pie chart
    # pichart(data, column="Estado")

    ## Relationship Plot (scatter plot)
    # relationship_plot(data, "ansiedad.rasgo", "ansiedad.estado")

    ## Boxplot based on column (Trait by Status)
    # box_plot_by_column(data, x_column="Sexo", y_column="ansiedad.estado")

    x, hue = "ansiedad.medicada", "Sexo"
    hue_order = ["M", "H"]
    diagnosed_female = data[data["Sexo"]=="M"]["ansiedad.medicada"]
    diagnosed_male = data[data["Sexo"]=="H"]["ansiedad.medicada"]
    diagnosed = pd.merge(diagnosed_female, diagnosed_male)
    
    diagnosed.value_counts().plot(kind="bar", stacked=True)
    plt.show()
    print(diagnosed)

    ## Scatter  Plot (Trait vs. Age)
    # relationship_plot(data, "ansiedad.rasgo", "Edad")

    ## Scatter Plot (Trait vs. Age)
    # relationship_plot(data, "ansiedad.estado", "Edad")

    ## Boxplot based on column (Age by Diagnosis)
    # box_plot_by_column(data, x_column="ansiedad.medicada", y_column="Edad")

