import pandas as pd
import numpy as np
from plotnine import *
from IPython.display import display


def basic_eda(df: pd.DataFrame):
    missing_ct = df.isnull().sum()
    dttm_cols = df.select_dtypes(include=np.datetime64).columns.tolist()
    num_cols = df.select_dtypes(include=[int, float]).columns.tolist()
    print('Remember to change the printouts to make sense for your data')
    print(f'Row count is {"{:,}".format(df.shape[0])}')
    print(f'{"{:,}".format(df.duplicated().sum())} of the rows are duplicates, about '
          f'{round(df.duplicated().sum() / df.shape[0] * 100, 2)}% of the total rows')
    print(f'{"{:,}".format(missing_ct.sum())} of the rows are missing, about '
          f'{round(missing_ct.sum() / df.shape[0] * 100, 2)}% of the total rows')
    for col in df.columns:
        print()
        print(str(col))
        print(f'There are {"{:,}".format(df[col].nunique())} unique {col}, approximately '
              f'{round(df[col].nunique() / df.shape[0] * 100)}% of the total {col} rows')
        print(f'{"{:,}".format(df[col].duplicated().sum())} of the {col} rows are duplicates, about '
              f'{round(df[col].duplicated().sum() / df.shape[0] * 100, 2)}% of the total {col} rows')
        print(f'{"{:,}".format(missing_ct[col])} of the {col} rows are missing, about '
              f'{round(missing_ct[col] / df.shape[0] * 100, 2)}% of the total {col} rows')
        if col in dttm_cols:
            print(f'{df[col].min()} - The first {col} occured')
            print(f'{df[col].max()} - The last {col} occured')
        elif col in num_cols:
            ljust_len = 38 + len(str(col))
            print(f'The minimum value of {col} is'.ljust(ljust_len) + f'{df[col].min()}')
            print(f'The maximum value of {col} is'.ljust(ljust_len) + f'{df[col].max()}')
            print(f'The mean value of {col} is'.ljust(ljust_len) + f'{df[col].mean()}')
            print(f'The median value of {col} is'.ljust(ljust_len) + f'{df[col].median()}')
            print(f'The standard deviation of {col} is'.ljust(ljust_len) + f'{df[col].std()}')


def eda_waffle(df: pd.DataFrame, flip: bool = False, remove_null: bool = True):
    unq_counts = df.nunique()
    for col in df.columns:
        if 1 < unq_counts[col] <= .05 * df.shape[0]:
            print(waffle_plot(df, col, flip=flip, remove_null=remove_null))


def eda_hist(df: pd.DataFrame, large_counts: bool = False, logy: bool = False):
    dttm_cols = df.select_dtypes(include=np.datetime64).columns.tolist()
    non_str_cols = df.select_dtypes(exclude='object').columns.tolist()
    for col in non_str_cols:
        df_tmp = pd.DataFrame({col: df[col]})
        if large_counts:
            val_cts = df[col].value_counts()
            lrg_vals = val_cts.loc[val_cts > val_cts.iloc[0] * 0.05].index
            df_tmp = df_tmp.loc[df_tmp[col].isin(lrg_vals)]
        unq_counts = df_tmp[col].nunique()
        if unq_counts > 5:
            bin_ct = min(unq_counts, 100)
            p = (ggplot(df_tmp, aes(x=col))
                 + geom_histogram(bins=bin_ct, fill='firebrick', color='darkgoldenrod')
                 + xlab(col)
                 + ylab('Count')
                 )
            if col in dttm_cols or len(str(df_tmp[col].iloc[0])) > 5:
                p += theme(axis_text_x=element_text(rotation=90, hjust=0.5))
            if logy:
                p += scale_y_log10()
            print(p)


def waffle_plot(df: pd.DataFrame, col_name: str, plot_title: str = None, flip: bool = False, remove_null: bool = True):
    if plot_title is None:
        plot_title = col_name
    x_min = np.array(list(range(0, 10)) * 10)
    x_max = np.array(x_min) + 0.9
    y_min = np.array([y for z in [[x] * 10 for x in range(10)] for y in z])
    y_max = np.array(y_min) + 0.9
    df_waffle = pd.DataFrame({'x_min': x_min, 'x_max': x_max, 'y_min': y_min, 'y_max': y_max})
    val_cts = df[col_name].value_counts()
    if remove_null:
        srs_prcnts = (val_cts / val_cts.sum() * 100).round().astype(int)
        total_prcnt = 100 - 1
    else:
        srs_prcnts = (val_cts / df.shape[0] * 100).round().astype(int)
        total_prcnt = (val_cts.sum() / df.shape[0] * 100).round().astype(int) - 1
    srs_prcnts = srs_prcnts.loc[srs_prcnts >= 1]
    srs_prcnts = srs_prcnts.cumsum() - 1
    df_waffle['clr'] = 'Null Values'
    df_waffle.loc[:total_prcnt, 'clr'] = f'The other {val_cts.shape[0] - srs_prcnts.shape[0]} values'
    for idx in srs_prcnts.index.tolist()[::-1]:
        df_waffle.loc[:srs_prcnts[idx], 'clr'] = idx
    p = (ggplot(df_waffle)
         + geom_rect(aes(xmin='x_min', ymin='y_min', xmax='x_max', ymax='y_max', fill='clr'))
         + theme(figure_size=(6, 6))
         + theme(axis_line=element_blank(),
                 axis_text=element_blank(),
                 axis_ticks=element_blank(),
                 panel_background=element_blank(),
                 legend_title=element_blank())
         + ggtitle(plot_title)
         )
    if flip:
        p += coord_flip()
    return p