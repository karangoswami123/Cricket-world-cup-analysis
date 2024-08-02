import pandas as pd

files = {
    "2003": "CRICKET WORLD CUP - 2003.csv",
    "2007": "CRICKET WORLD CUP - 2007.csv",
    "2011": "CRICKET WORLD CUP - 2011.csv",
    "2015": "CRICKET WORLD CUP - 2015.csv",
    "2019": "CRICKET WORLD CUP - 2019.csv",
}

def load_data():
    dataframes = {}
    for year, file_path in files.items():
        try:
            dataframes[year] = pd.read_csv(file_path)
            print(f"Loaded data for year {year}")
        except FileNotFoundError:
            print(f"File not found for year {year}: {file_path}")
        except pd.errors.EmptyDataError:
            print(f"No data found in file for year {year}: {file_path}")
        except Exception as e:
            print(f"Error loading data for year {year}: {e}")
    return dataframes
