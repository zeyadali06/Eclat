import pandas as pd


class PreparData:

    @staticmethod
    def is_vertical(df: pd.DataFrame) -> bool:
        # Check if the dataframe is vertical
        return True

    @staticmethod
    def to_vertical(df: pd.DataFrame) -> pd.DataFrame:
        # Convert the parametarized horizontal dataframe to vertical dataframe
        return df
