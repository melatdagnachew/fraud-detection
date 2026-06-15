import pandas as pd


def convert_datetime(df, columns):

    for col in columns:

        try:
            df[col] = pd.to_datetime(df[col])

        except Exception as e:
            print(
                f"Failed converting {col}: {e}"
            )

    return df


def remove_duplicates(df):

    before = len(df)

    df = df.drop_duplicates()

    after = len(df)

    print(
        f"Removed {before-after} duplicates"
    )

    return df


def check_missing_values(df):

    return df.isnull().sum()
