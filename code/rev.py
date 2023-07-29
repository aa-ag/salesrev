############ ------------ IMPORTS ------------##################################
import importlib.util as u
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt


############ ------------ FUNCTION(S) ------------##############################
def test_env():
    pckgs = ["pandas", "numpy", "matplotlib", "seaborn"]
    print("\n")
    for pckg in pckgs:
        spec = u.find_spec(pckg)
        if spec is None:
            print(f'"{pckg}" is not installed')
            return False
        else:
            continue
            # print(f'"{pckg}" is installed')
    return True


def check_inputs():
    df = pd.read_csv("files/advertising.csv")
    print(df.info(verbose=True))
    print(df.describe())
    print(df.head(5))


def clean_inputs():
    df = pd.read_csv("files/advertising.csv")
    df.drop(["Unnamed: 0"], axis=1, inplace=True)
    return df.head()


def analyse(data):
    # plt.show()
    fig = sns.displot(data.Sales, kind="kde")
    fig.savefig("./files/sales_plot.png")


# ------------ DRIVER CODE ------------##############################ß
if __name__ == "__main__":
    if test_env():
        # check_inputs()
        data = clean_inputs()
        analyse(data)
