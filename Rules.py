import pandas as pd
from Eclat import Eclat


class Rules:
    # Rules
    # if first --> second
    first = []
    second = []
    lift = 0.0
    confidnce = 0.0

    def __init__(self, df: pd.DataFrame, fir: list, sec: list) -> None:
        # df: the main dataframe
        self.first = fir
        self.second = sec
        self.lift = self.calc_lift(df)
        self.confidnce = self.calc_conf(df)

    def calc_lift(self, df: pd.DataFrame) -> float:
        return Eclat.calc_prob(df, [self.first, self.second]) / (Eclat.calc_prob(df, [self.first]) * Eclat.calc_prob(df, [self.second]))

    def calc_conf(self, df: pd.DataFrame) -> float:
        return Eclat.calc_support(df, [list(set(self.first + self.second))]) / Eclat.calc_support(df, self.first)
