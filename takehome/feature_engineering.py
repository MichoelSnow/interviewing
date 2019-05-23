import pandas as pd
import numpy as np
from pandas.tseries.holiday import USFederalHolidayCalendar as FedCal


def fe_dt(df_in: pd.DataFrame):
    df = df_in.copy()
    dttm_cols = df.select_dtypes(include=np.datetime64).columns.tolist()
    for col in dttm_cols:
        df[col + '_year'] = df[col].dt.year
        df[col + '_month'] = df[col].dt.month
        df[col + '_day'] = df[col].dt.day
        df[col + '_hour'] = df[col].dt.hour
        df[col + '_minute'] = df[col].dt.minute
        df[col + '_second'] = df[col].dt.second
        df[col + '_date'] = df[col].dt.date
        df[col + '_time'] = df[col].dt.time
        df[col + '_dayofyear'] = df[col].dt.dayofyear
        df[col + '_weekofyear'] = df[col].dt.weekofyear
        df[col + '_dayofweek'] = df[col].dt.dayofweek  # Monday=0, Sunday=6
        df[col + '_quarter'] = df[col].dt.quarter
        df[col + '_ismonthstart'] = df[col].dt.is_month_start
        df[col + '_ismonthend'] = df[col].dt.is_month_end
        df[col + '_isquarterstart'] = df[col].dt.is_quarter_start
        df[col + '_isquarterend'] = df[col].dt.is_quarter_end
        df[col + '_isyearstart'] = df[col].dt.is_year_start
        df[col + '_isyearend'] = df[col].dt.is_year_end
        df[col + '_isleapyear'] = df[col].dt.is_leap_year
        df[col + '_isusfederalholiday'] = check_holidays(df, col)
    return df


def check_holidays(df: pd.DataFrame, col: str):
    start_date = df[col].min()
    end_date = df[col].max()
    hol_list = FedCal().holidays(start=start_date, end=end_date)
    return df[col].isin(hol_list)
