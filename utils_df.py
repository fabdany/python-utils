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

def apply_function_to_create_column(df,function,col,result_col):
  """
  Parameters
     ----------
     df : a pandas dataframe
     function : a function to apply to a column
     col : a column name on which the function is applied
     result_col : a column added that contains the values returned from applying the function on the column
     -------
     Modifies the dataframe.
     Use Case: when you need to apply the same function to several columns in order to create new columns
  """ 
  df[result_col]=df.apply(lambda x: function(x[col]), axis=1) 

def group_sum(df,groupby_list,sum_list):
  """
  Parameters
     ----------
     df : a pandas dataframe
     groupby_list : a list of columns 
     sum_list : a list of colums on which the sum should be applied
     -------
    Returns a new dataframe with sums of values for columns in sum_list, grouped by the values contained in the columns listed in groupby_list
  """
  var_list=groupby_list+sum_list
  df1=df[var_list].groupby(groupby_list).sum()
  df2=pd.DataFrame(df1.reset_index(),columns=var_list)
  return df2


def group_count(df,groupby_list,count_var_name):
  """
  Parameters
     ----------
     df : a pandas dataframe
     groupby_list : a list of columns 
     count_var_name : a column name that will contain counts
     -------
  Returns a new dataframe with counts in column count_var_name, grouped by the values contained in the columns listed in groupby_list
  """
  df[count_var_name]=1
  var_list=groupby_list+[count_var_name]
  df1=df[var_list].groupby(groupby_list).sum()
  df2=pd.DataFrame(df1.reset_index(),columns=var_list)
  return df2


def group_max(df,groupby_list,max_list):
  """
  Parameters
     ----------
     df : a pandas dataframe
     groupby_list : a list of columns 
     max_list : a list of column names for which we want to find maximum values
     -------
  Returns a new dataframe with maximum values, grouped by the values contained in the columns listed in groupby_list
  """
  var_list=groupby_list+max_list
  df1=df[var_list].groupby(groupby_list).max()
  df2=pd.DataFrame(df1.reset_index(),columns=var_list)
  return df2

def group_min(df,groupby_list,min_list):
  """
  Parameters
     ----------
     df : a pandas dataframe
     groupby_list : a list of columns 
     min_list : a list of column names for which we want to find minimum values
     -------
  Returns a new dataframe with minimum values, grouped by the values contained in the columns listed in groupby_list
  """
  var_list=groupby_list+min_list
  df1=df[var_list].groupby(groupby_list).min()
  df2=pd.DataFrame(df1.reset_index(),columns=var_list)
  return df2

def group_mean(df,groupby_list,mean_list):
  """
  Parameters
     ----------
     df : a pandas dataframe
     groupby_list : a list of columns 
     mean_list : a list of colums for which the mean function should be calculated
     -------
    Returns a new dataframe with means of values for columns in mean_list, grouped by the values contained in the columns listed in groupby_list
  """
  var_list=groupby_list+mean_list
  df1=df[var_list].groupby(groupby_list).mean()
  df2=pd.DataFrame(df1.reset_index(),columns=var_list)
  return df2
