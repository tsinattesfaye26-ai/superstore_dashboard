import pandas as pd


def load_and_clean_data():
    # Load the original Excel file
    df = pd.read_excel("data/Sample_Superstore.xlsx")

    # Clean column names
    df.columns = df.columns.str.strip()

    # Remove completely empty rows
    df = df.dropna(how="all")

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Convert date columns
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])

    return df

