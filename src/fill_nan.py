

import pandas as pd

# daily_patients,treated_patients,discharged_patients,deaths
def fill_nan_values(df_hospital):
    df_hospital.fillna(value = {'daily_patients' : df_hospital.daily_patients.mode()[0],
                                'treated_patients' : df_hospital.treated_patients.mode()[0],
                                'discharged_patients' : pd.to_numeric(df_hospital.discharged_patients , errors='coerce').mean(),
                                'deaths' : pd.to_numeric(df_hospital.deaths , errors='coerce').mean(),

                                } , inplace = True)
    
    return df_hospital