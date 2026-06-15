import pandas as pd


def load_csv(path):
    """
    Load CSV safely.
    """

    try:
        df = pd.read_csv(path)

        print(f"Loaded: {path}")
        print(f"Shape: {df.shape}")

        return df

    except FileNotFoundError:
        raise FileNotFoundError(
            f"Dataset not found: {path}"
        )

    except Exception as e:
        raise RuntimeError(
            f"Error loading {path}: {e}"
        )
