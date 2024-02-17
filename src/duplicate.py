

import pandas as pd


def show_duplicate_data(df_hospital):
    duplicate_record = df_hospital.duplicated()
    return duplicate_record.sum()