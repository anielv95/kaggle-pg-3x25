import functions as f
import numpy as np
import pandas as pd


def test_base_line():
    input_var = np.zeros((2, 2))
    assert (np.array([4.647, 4.647]) == f.base_line(input_var)).all()
    input_var = pd.DataFrame(data={"col1": [1, 2], "col2": [1, 2]})
    assert (np.array([4.647, 4.647]) == f.base_line(input_var)).all()
