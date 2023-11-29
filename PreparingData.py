import pandas as pd


class PreparData:

    @staticmethod
    def is_horizontal(df: pd.DataFrame) -> bool:
        # Check if the dataframe is horizontal
        return True

    @staticmethod
    def convert_to_vertical(df: pd.DataFrame) -> pd.DataFrame:
        # Convert the parametarized vertical dataframe to horizontal dataframe
        return df
