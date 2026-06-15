def create_time_since_signup(df):

    df["time_since_signup"] = (
        df["purchase_time"]
        -
        df["signup_time"]
    ).dt.total_seconds()

    return df


def create_hour_feature(df):

    df["hour_of_day"] = (
        df["purchase_time"].dt.hour
    )

    return df


def create_day_feature(df):

    df["day_of_week"] = (
        df["purchase_time"].dt.dayofweek
    )

    return df


def create_user_transaction_count(df):

    df["user_transaction_count"] = (
        df.groupby("user_id")
        ["user_id"]
        .transform("count")
    )

    return df
