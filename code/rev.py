############ ------------ IMPORTS ------------##################################
import importlib.util as u
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt


############ ------------ FUNCTION(S) ------------##############################
def test_env():
    # TODO: this will be moved to "tests" eventually
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
    df.drop(["N"], axis=1, inplace=True)
    return df.head()


def initial_analysis(data):
    dataframe_columns = data.columns.to_list()
    for each_column in dataframe_columns:
        fig = sns.displot(data[each_column], kind="kde")
        fig.savefig(f"./files/{each_column}_plot.png")


def explore_predictor_response_relationship(data):
    sns.pairplot(
        data,
        x_vars=["TV", "radio", "newspaper"],
        y_vars="sales",
        height=7,
        aspect=1,
        kind="reg"
    )
    plt.show()


# ------------ DRIVER CODE ------------##############################ß
if __name__ == "__main__":
    if test_env():
        # check_inputs()
        data = clean_inputs()
        # initial_analysis(data)
        explore_predictor_response_relationship(data)
