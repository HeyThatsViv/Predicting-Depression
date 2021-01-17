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
    Also sets the index to be the SEQN column.
    
    Args:
        path (str): Location on computer where files are located.
        file_str (str): Specific search query of which files to find.
        
    Returns:
        Displays the files that were found for verification and returns the 
        DataFrame of all files after pd.concat is performed and the index is set.
    
    Example:
        combined_df = glob_concat(r'File/File', '*.XPT')
    '''
    
    files = glob.glob(os.path.join(path, file_str))
    display(files)
    df_files = [pd.read_sas(file) for file in files]
    combined_df = pd.concat(df_files)
    combined_df.SEQN = combined_df.SEQN.astype('int64')
    combined_df.set_index('SEQN', verify_integrity=True, inplace=True)
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


def first_cancer_count(x):
    '''
    Function for creating a new column that is a count from the first cancer
    information of people that have had a first cancer.
    
    Args:
        x(row in DataFrame): Pass over each entry in DataFrame to count if a
            first cancer is recorded.
        
    Returns:
        1 if information of a first cancer exists and 0 if it does not.
    
    Example:
        df.apply(first_cancer_count, axis=1)
    '''

    if x['first_cancer_type'] != 'None':
        return 1
    else:
        return 0


def second_cancer_count(x):
    '''
    Function for creating a new column that is a count from the second cancer
    information of people that have had a second cancer.
    
    Args:
        x(row in DataFrame): Pass over each entry in DataFrame to count if a
            second cancer is recorded.
        
    Returns:
        1 if information of a second cancer exists and 0 if it does not.
    
    Example:
        df.apply(second_cancer_count, axis=1)
    '''

    if x['second_cancer_type'] != 'None':
        return 1
    else:
        return 0


def third_cancer_count(x):
    '''
    Function for creating a new column that is a count from the third cancer
    information of people that have had a third cancer.
    
    Args:
        x(row in DataFrame): Pass over each entry in DataFrame to count if a
            third cancer is recorded.
        
    Returns:
        1 if information of a third cancer exists and 0 if it does not.
    
    Example:
        df.apply(third_cancer_count, axis=1)
    '''

    if x['third_cancer_type'] != 'None':
        return 1
    else:
        return 0