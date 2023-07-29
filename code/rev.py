############ ------------ IMPORTS ------------##################################
import importlib.util as u
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


############ ------------ GLOBAL VARIABLE(S) ------------#######################


############ ------------ FUNCTION(S) ------------##############################
def test_env():
    pckgs = ["pandas", "numpy", "matplotlib"]
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
    df = pd.read_csv("inputs/advertising.csv")
    print(df.info(verbose=True))
    print(df.describe())
    print(df.head(5))


def clean_inputs():
    df = pd.read_csv("inputs/advertising.csv")
    df.drop(["Unnamed: 0"], axis=1, inplace=True)
    print(df.head())


# ------------ DRIVER CODE ------------##############################ß
if __name__ == "__main__":
    if test_env():
        # check_inputs()
        clean_inputs()
