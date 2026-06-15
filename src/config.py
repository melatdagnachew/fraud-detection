from pathlib import Path

# Paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"
MODELS_DIR = PROJECT_ROOT / "models"

# Files
FRAUD_DATA = RAW_DATA_DIR / "Fraud_Data.csv"
IP_DATA = RAW_DATA_DIR / "IpAddress_to_Country.csv"
CREDITCARD_DATA = RAW_DATA_DIR / "creditcard.csv"

# Columns
FRAUD_TARGET = "class"
CREDIT_TARGET = "Class"

DATETIME_COLS = [
    "signup_time",
    "purchase_time"
]

CATEGORICAL_COLS = [
    "source",
    "browser",
    "sex",
    "country"
]
