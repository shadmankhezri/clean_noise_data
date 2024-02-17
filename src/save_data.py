# whit this def we save the final clean data in the new csv file

import pandas as pd


final_path = "data/hospital_final.csv"

def save_final_hospital_data(df_hospital):
    df_hospital.to_csv(final_path , index = False)