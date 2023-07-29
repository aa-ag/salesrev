############ ------------ IMPORTS ------------##################################
import importlib.util as u
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


############ ------------ FUNCTION(S) ------------##############################
def test_env():
    # TODO: this will be moved to "tests" eventually
    pckgs = ["pandas", "numpy", "matplotlib", "seaborn", "sklearn"]
    print("\n")
    for pckg in pckgs:
        spec = u.find_spec(pckg)
        if spec is None:
            print(f'{pckg} is not installed')
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
    return df


def initial_analysis(data):
    dataframe_columns = data.columns.to_list()
    for each_column in dataframe_columns:
        fig = sns.displot(data[each_column], kind="kde")
        fig.savefig(f"./files/{each_column}_plot.png")


def explore_predictor_response_relationship(data):
    fig = sns.pairplot(
        data,
        x_vars=["TV", "radio", "newspaper"],
        y_vars="sales",
        height=4,
        aspect=0.5,
        kind="reg"
    )
    fig.savefig("./files/predictor_response_relationship_plot.png")


def plot_correlations(data):
    # print(data.corr())
    sns.heatmap(data.corr(), annot=True)
    plt.show()


def create_linear_regression_model(data):
    x = data[["TV"]]
    y = data.sales
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)
    linear_regression = LinearRegression()
    linear_regression.fit(x_train, y_train)
    return linear_regression


def calculate_intercept_and_coefficient(linear_regression):
    print(f"Intercept: {round(linear_regression.intercept_, 2)}")
    print(f"Coefficient: {round(linear_regression.coef_[0], 2)}")


# ------------ DRIVER CODE ------------##############################ß
if __name__ == "__main__":
    if test_env():
        # check_inputs()
        data = clean_inputs()
        # initial_analysis(data)
        # explore_predictor_response_relationship(data)
        # plot_correlations(data)
        linear_regression = create_linear_regression_model(data)
        calculate_intercept_and_coefficient(linear_regression)
