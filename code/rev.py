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


# ------------ DRIVER CODE ------------##############################ß
if __name__ == "__main__":
    test_env()
