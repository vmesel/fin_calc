import pandas as pd


def generate_dataset_with_patrimony():
    df = pd.DataFrame()
    df["patrimony"] = [100100, 101100, 102000, 103100, 105000]
    df["movements"] = [0, 0, 900, 0, 0]
    return df


def generate_dataset_with_patrimony_and_periodic_contributions():
    df = pd.DataFrame()
    df["patrimony"] = [100100, 101100, 102000, 103100, 105000]
    df["movements"] = [0, 0, 900, 0, 0]
    df["contribution"] = [100, 100.999001, 100.999001, 102.0882059, 103.9695599]

    return df
