import numpy as np
import pandas as pd

"""
paper example
"""
def paper_example():
    values = np.random.randn(700)
    values[0:391] = values[0:391] * np.sqrt(1.0)
    values[391:518] = values[391:518] * np.sqrt(0.365)
    values[518:701] = values[518:701] * np.sqrt(1.033)

    rng = pd.date_range('1/1/2017', periods=700, freq='H')

    df = pd.DataFrame({'Vals' : values, 'Ts' : rng})
    return df
