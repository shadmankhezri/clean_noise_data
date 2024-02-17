# make this def for fill missing values by mode or mean

# for "discharged_patients" and "deaths" We need to make sure that it only uses
# values that are numeric with "pd.to_numeric" and does not consider nan values because we want to get an average.


import pandas as pd

def fill_nan_values(df_hospital):
    df_hospital.fillna(value = {
                                'daily_patients' : df_hospital.daily_patients.mode()[0],
                                'treated_patients' : df_hospital.treated_patients.mode()[0],
                                'discharged_patients' : pd.to_numeric(df_hospital.discharged_patients , errors='coerce').mean(),
                                'deaths' : pd.to_numeric(df_hospital.deaths , errors='coerce').mean(),

                                } , inplace = True)
    
    return df_hospital