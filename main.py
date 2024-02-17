
from src.read_data import read_csv_data
from src.duplicate import show_duplicate_data
# from src.count_duplicate import *



PATH = "data/hospital.csv"

def main():

    df_hospital = read_csv_data(PATH)
    print("\nFirst Hospital Data: \n")
    print(df_hospital)
    print(100*"*")



    duplicate_records = show_duplicate_data(df_hospital)
    print("\nShow Counts of Duplicated Records:")
    print(duplicate_records)
    print(100*"*")


    



if __name__ == "__main__":
    main()