import pandas as pd

def renameColumns (df):
    new_columns = []
    for col in df.columns:
        new_col = col[1]
        new_columns.append(new_col)
    df.columns = new_columns
    df = df.fillna(0)

#Method to fetch data grom a given URL. This is specific to FB_REF website
def fetchDataFromUrl (URL):
    df = pd.read_html(URL)[4]
    renameColumns(df)
    return (df)