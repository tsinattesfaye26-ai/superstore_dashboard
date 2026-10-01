import pandas as pd


def load_raw_data():
    df = pd.read_excel("data/raw/Sample_Superstore.xlsx")
    return df

def clean_data(df):

    # Clean column names
    df.columns = df.columns.str.strip()

    # Fill missing Burlington, Vermont postal codes
    df["Postal Code"] = df["Postal Code"].fillna(5401)

    # Remove completely empty rows
    df = df.dropna(how="all")

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Convert dates
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])

    return df


def get_clean_data():

    df = load_raw_data()

    df = clean_data(df)

    return df