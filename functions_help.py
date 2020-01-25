


## A Look at the columns of Data
def list_cols(num_cols):
    '''
    INPUT:
    num_cols - int the number of cols in df

    This function will print a columns of the dataset.
    '''
    print(num_cols)

    
def list_cols_with_missing_values(df):
    '''
    INPUT:
    Dataframe - in df

    This function will print a columns has missing values.
    '''
    df.columns[df.isna().any()].tolist()