# with "show_nan_values" just display all records that have nan value

# with "show_sum_nan_values" display count of nan values 

import pandas as pd


def show_nan_values(df_hospital):
    return df_hospital[df_hospital.isnull().any(axis=1)]



def show_sum_nan_values(df_hospital):
    sum_nan_value = df_hospital.isnull().sum()
    return sum_nan_value[sum_nan_value > 0]