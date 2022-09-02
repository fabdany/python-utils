# -*- coding: utf-8 -*-
import pandas as pd
import copy as cp
import numpy as np

def delete_df_cols(old_df, cols):
  #substract a list of columns from the list of old dataframe columns
  """
  Parameters
     ----------
     old_df : pandas.core.frame.DataFrame
         Two-dimensional size-mutable,
         potentially heterogeneous tabular data
     cols : list of column names
         Remove all the columns in that list from the dataframe.
     -------
     Returns a new dataframe
  """
  new_df=pd.DataFrame()
  new_df=old_df
  new_cols=[item for item in new_df.columns.values if item not in cols]
  new_df=new_df[new_cols]
  return new_df

# Defining functions to fill empty cells of a dataframe. Needs to be provided with a dataframe, a list of columns, and the value used to fill
def fillna_in_cols(df,cols,fill):
  """
  Parameters
     ----------
     df : pandas.core.frame.DataFrame
         Two-dimensional size-mutable,
         potentially heterogeneous tabular data
     cols : list of column names 
         Fills null values in these columns with the fill value.
     fill : 
      The fill value
     -------
     Returns the same dataframe with na values filled
  """
  for c in cols:
    df[c].fillna(fill, inplace=True)
  return df

def save_xls_multi_sheet(dico,file):
  """
  Parameters
     ----------
     dico : a dictionnary with keys as names of sheets and with values as pandas dataframes
     file : a filepath to an excel file with multiple sheets built from several pandas dataframes
     -------
     Creates an Excel file from multiple pandas dataframe
  """
  writer = pd.ExcelWriter(file)
  for key, value in dico.items():
    value.to_excel(writer, sheet_name=key, index=False)
  writer.save() 
