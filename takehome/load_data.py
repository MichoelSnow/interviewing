# import pandas as pd
# from IPython.display import display


def check_files(file_paths: list):
    """
    Before loading any data into memory it's a good idea to get an idea of the amount of data, to make sure that it
    will fit into memory, as well as what the data looks like, which make sure there's nothing weird or unusual about
    the data, e.g., pipe delimiters instead of commas.
    """
    for fl in file_paths:
        print(f"!wc -l {fl}")
        print(f"!head -3 {fl}")
        print("print()")


def read_csvs(file_paths: list, df_names: list):
    """
    I like to load in everything as strings, so that pandas doesn't "helpfully" convert data types which should be
    strings into integers, e.g., ids which contain leading zeros.
    """
    for idx, fl in enumerate(file_paths):
        print(f"{df_names[idx]} = pd.read_csv('{fl}', dtype=str)")


def change_column_names(df_names: list, old_cols: list, new_cols: list):
    for df in df_names:
        for idx, col in enumerate(old_cols):
            print(f"{df} = {df}.rename(columns = '{col}': '{new_cols[idx]}'")


def convert_str_to_dt(df_names: list, dt_cols: list, str_format: str):
    # Go to http://strftime.org/ for the list of format abbreviations
    for df in df_names:
        for col in dt_cols:
            print(f"{df}.{col} = pd.to_datetime({df}.{col}, format='{str_format}')")


def convert_epoch_to_dt(df_names: list, dt_cols: list):
    for df in df_names:
        for col in dt_cols:
            print(f"{df}.{col} = pd.to_datetime({df}.{col}, unit=s)")


def display_df_head(df_names: list):
    for df in df_names:
        print(f"display({df}.head())")

