

import pandas as pd


def drop_duplicated_records(df_hospital):
    return df_hospital.drop_duplicates(keep = 'first' , inplace = True)