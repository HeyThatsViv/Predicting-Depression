'''
Functions written for use in this project to predict patient depression based on medical data
    -Vivienne DiFrancesco
    -viviennedifrancesco@gmail.com'''

import glob, os
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

def glob_concat(path, file_str):
    '''
    Looks for files in folder path and combines them into a DataFrame.
    
    Args:
        path (str): Location on computer where files are located.
        file_str (str): Specific search query of which files to find.
        
    Returns:
        Displays the files that were found for verification and returns the 
        DataFrame of all files after pd.concat is performed.
    
    Example:
        combined_df = glob_concat(r'File/File', '*.XPT')
    '''
    
    files = glob.glob(os.path.join(path, file_str))
    display(files)
    df_files = [pd.read_sas(file) for file in files]
    combined_df = pd.concat(df_files)
    return combined_df


def val_counts(df):
    '''
    Display value counts for all the columns in a DataFrame.

    Args:
        df (DataFrame): DataFrame to perform .value_counts() on each column. 

    Returns:
        Value counts for each column with some visual cues between columns.
    '''

    for col in df.columns:
        print(f'{col} value counts', '\n')
        display(df[col].value_counts(dropna=False))
        print('--------------------------------------')


def cols_tokeep(df, col_list):
    '''
    Makes a copy of the passed in DataFrame and drops all columns except those
    specified in a list.
    
    Args:
        df(DataFrame): DataFrame to take specific columns from.
        col_list(list): List of columns in the DataFrame to be kept.
    
    Returns:
        New DataFrame that has only the columns specified from the col_list.
    
    Example:
        new_df = cols_tokeep(old_df, columns_list)
    '''
    df_copy = df.copy()
    for col in df_copy.columns:
        if col not in col_list:
            df_copy.drop(columns=[col], inplace=True)
        else:
            pass
    return df_copy