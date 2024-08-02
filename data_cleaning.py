import pandas as pd

def clean_data(df):
    try:
        # Drop rows with all NaN values
        df.dropna(how='all', inplace=True)

        # Drop rows with NaN in essential columns
        df.dropna(subset=['TEAM', 'RUNS SCORED', 'WICKETS LOST', 'WICKETS TAKEN', 'AGAINST', 'RESULT', 'VENUE'], inplace=True)

        # Convert columns to appropriate data types
        df['RUNS SCORED'] = pd.to_numeric(df['RUNS SCORED'], errors='coerce')
        df['WICKETS LOST'] = pd.to_numeric(df['WICKETS LOST'], errors='coerce')
        df['WICKETS TAKEN'] = pd.to_numeric(df['WICKETS TAKEN'], errors='coerce')

        # Reset index
        df.reset_index(drop=True, inplace=True)
    except KeyError as e:
        print(f"Missing expected column: {e}")
    except Exception as e:
        print(f"Error cleaning data: {e}")
    return df
