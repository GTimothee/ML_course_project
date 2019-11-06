import pandas as pd
import numpy as np

def check_dataset(dataset):
    assert len(dataset) == 2
    train, test = dataset
    assert len(train) == 2 and len(test) == 2
    x_train, y_train = train
    x_test, y_test = test
    assert len(x_train) == len(y_train) and len(x_test) == len(y_test)
    assert len(x_test) < len(x_train)
    assert type(y_train) == type(y_test)
    assert type(y_train) == pd.core.series.Series or type(y_train) == np.ndarray
    assert type(x_train) == type(x_test) == pd.core.frame.DataFrame
    assert len(x_train.columns) == len(x_test.columns)