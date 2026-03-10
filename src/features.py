import pandas as pd

def get_score(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['Score'] = df['gh'].astype(str) + ' - ' + df['ga'].astype(str)
    return df
