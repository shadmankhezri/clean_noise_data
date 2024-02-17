# import functions from src
#-----------------------------------------------
from src.read_data import read_csv_data
from src.duplicate import show_duplicate_data
from src.drop_duplicate import drop_duplicated_records
from src.show_nan import show_nan_values , show_sum_nan_values
from src.fill_nan import fill_nan_values
from src.save_data import save_final_hospital_data
from src.display import display
#-----------------------------------------------

path = "data/hospital.csv"

#-----------------------------------------------
# create the main function for call src functions 

def main():
#-----------------------------------------------
# calling "read_csv_data" function from "read_data" for show the first hospital file
    
    df_hospital = read_csv_data(path)
    display(f"\nFirst Hospital Data:\n\n{df_hospital}")

#-----------------------------------------------
# calling "show_duplicate_data" function from "duplicate" for show duplicated records
    
    duplicate_records = show_duplicate_data(df_hospital)
    display(f"Show Counts of Duplicated Records:\n{duplicate_records}")

#-----------------------------------------------
# calling "drop_duplicated_records" function from "drop_duplicate" for drop duplicated records

    drop_duplicated_records(df_hospital)
    display("Drop duplicated records successfully")
    
#-----------------------------------------------
# Calling the "show_nan_values" function from "show_nan" to display records that have nan values

    show_missing_values = show_nan_values(df_hospital)
    display(f"Show records that have a null value:\n\n{show_missing_values}")

#-----------------------------------------------
# Calling the "show_sum_nan_values" function from "show_nan" to display the number of nans

    show_number_missing_value = show_sum_nan_values(df_hospital)
    display(f"Show the number of missing values for each columns:\n\n{show_number_missing_value}")

#-----------------------------------------------
# calling the "fill_nan_values" function from "fill_nan" for fill the records that have nan value
    
    fill_nan_recordes = fill_nan_values(df_hospital)
    display(f"Fill nan data with mode and mean:\n\n{fill_nan_recordes}")

#-----------------------------------------------
# Calling the "show_sum_nan_values" function from "show_nan" again to ensure nan records are filled
    
    show_number_missing_value = show_sum_nan_values(df_hospital)
    display(f"Show the number of missing values for each columns:\n\n{show_number_missing_value}")

#-----------------------------------------------
# calling the "save_final_hospital_data" function from "save_data" for save in the new csv file
    
    save_final_hospital_data(df_hospital)
    display("Save the final data in the new csv file successfully")

#-----------------------------------------------
if __name__ == "__main__":
    main()