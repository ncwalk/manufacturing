from pathlib import Path
import pandas as pd


def import_csv(file_path: (str, Path), columnname, **kwargs):
    """

    :param file_path: the path to the file on the local file system
    :param columnname: the column name to which the data is associated
    :param kwargs: keyword arguments to be passed directly into `pandas.read_csv()`
    :return: a pandas series of the data which is to be analyzed
    """
    df = pd.read_csv(file_path, **kwargs)
    return df[columnname]
