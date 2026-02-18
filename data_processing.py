'''
Filename: data_processing.py
Author: Elton Nichols
Date: 2026-02-16
Version: 1.0
Description: Data processing functions for use in exercises from AD450,
 North Seattle College, Winter 2026
'''
import pandas as pd

def rename_columns(df: pd.DataFrame):
    df.columns = df.columns.str.replace('Original titlÊ', 'original_title')
    df.columns = df.columns.str.replace('Genrë¨', 'genre')
    df.columns = df.columns.str.replace('Unnamed: 8', 'unnamed_8')
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.replace(' ', '_')
    return df

def remove_fully_null_columns_rows(df: pd.DataFrame):
    df = df.dropna(axis = 1, how = 'all')
    return df

def clean_and_fill_content_rating(df: pd.DataFrame):
    df1 = df.copy()
    df1['content_rating'] = df['content_rating'].fillna('Unrated')
    df1['content_rating'] = df['content_rating'].str.replace('Not Rated', 'Unrated')
    return df1

def clean_release_year(df: pd.DataFrame):
    df1 = df.copy()
    df1['release_year_coerce'] = pd.to_datetime(df['release_year'],
                                                errors = 'coerce')
    df1['release_year_mixed'] = pd.to_datetime(df['release_year'],
                                                errors = 'coerce', format = 'mixed')
    return df1

def clean_income(df: pd.DataFrame):
    df1 = df.copy()
    df1['income'] = df['income'].astype(str).str.replace(r'[^0-9]', '', regex = True)
    df1['income'] = pd.to_numeric(df1['income'], errors = 'coerce')
    df1['income'] = df['income'].astype('Int64')
    return df1
