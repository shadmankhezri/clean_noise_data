
from src.read_data import read_csv_data
from src.duplicate import show_duplicate_data
from src.drop_duplicate import drop_duplicated_records
from src.show_nan import show_nan_values , show_sum_nan_values
from src.fill_nan import fill_nan_values
from src.save_data import save_final_hospital_data
from src.display import display

path = "data/hospital.csv"



def main():

    df_hospital = read_csv_data(path)
    # print("\nFirst Hospital Data: \n")
    # print(df_hospital)
    # print(100*"*")

    # display("\nFirst Hospital Data: \n")
    # display(df_hospital)

    display(f"\nFirst Hospital Data:\n\n{df_hospital}")



    duplicate_records = show_duplicate_data(df_hospital)
    # print("\nShow Counts of Duplicated Records:")
    # print(duplicate_records)
    # print(100*"*")

    display(f"\nShow Counts of Duplicated Records:\n{duplicate_records}")
    # display(duplicate_records)



    drop_duplicated_records(df_hospital)
    print("Drop duplicated records successfully\n")
    print(100*"*")


    show_missing_values = show_nan_values(df_hospital)
    print("Show records that have a null value\n")
    print(show_missing_values)
    print(100*"*")


    show_number_missing_value = show_sum_nan_values(df_hospital)
    print("Show the number of missing values for each columns:\n")
    print(show_number_missing_value)
    print(100*"*")


    fill_nan_recordes = fill_nan_values(df_hospital)
    print("Fill nan data with mode and mean:\n")
    print(fill_nan_recordes)
    print(100*"*")


    show_number_missing_value = show_sum_nan_values(df_hospital)
    print("Show the number of missing values for each columns:\n")
    print(show_number_missing_value)
    print(100*"*")


    save_final_hospital_data(df_hospital)
    print("Save the final data in the new csv file successfully")

if __name__ == "__main__":
    main()