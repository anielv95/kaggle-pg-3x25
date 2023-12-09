import pandas as pd
import numpy as np


def base_line(df: pd.DataFrame):
    shape = df.shape
    value = 4.647
    # print(np.ones(shape) * value)
    return np.ones(shape[0]) * value
