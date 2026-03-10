import pandas as pd
from pathlib import Path

def load_raw_data(filename: str, sep=",") -> pd.DataFrame:

    project_root = Path(__file__).resolve().parents[1]
    data_path = project_root / "data" / "raw" / filename

    df = pd.read_csv(data_path, sep=sep)
    return df

if __name__ == "__main__":
    df = load_raw_data("UEFA.csv")
    clubs = load_raw_data("uefacompetitionclubs.csv", sep=";")
    games = load_raw_data("uefacompetitionresults.csv", sep=";")
    
    print(df.head())
    print(clubs.head())
    print(games.head())
    

    

