import pandas as pd

# import numpy as np


def base_line(df: pd.DataFrame):
    pred = df.copy()
    pred["Hardness"] = 4.647
    return pred[["id", "Hardness"]]


# def getting_csv(prediction):
#     df = pd.DataFrame(data={"Hardness":prediction})
#     df["id"] = df.index
