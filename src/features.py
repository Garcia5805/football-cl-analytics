import pandas as pd
import numpy as np

#Format Score as x - y
def get_score(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['Score'] = df['gh'].astype(str) + ' - ' + df['ga'].astype(str)
    return df

#Shows the winning team name and goal difference
def match_result(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    home = pd.to_numeric(df['gh'], errors='coerce').astype('Int64')
    away = pd.to_numeric(df['ga'], errors='coerce').astype('Int64')

    df['Winner'] =  np.where(home > away, df['Home'], 
                    np.where(home < away, df['Away'], 'Draw'))

    return df

#Format Date as MM/DD/YY
def format_date(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
    
    Month = df['Date'].dt.month
    Day = df['Date'].dt.day
    Year = df['Date'].dt.year % 100

    df['Date'] = Month.astype(str) + '/' + Day.astype(str) + '/' + Year.astype(str)
    return df