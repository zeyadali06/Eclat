import pandas as pd
from Eclat import Eclat


class Rules:
    # Rules
    # if first --> second
    first = []
    second = []
    lift = 0.0
    confidnce = 0.0

    def __init__(self, df: pd.DataFrame, fir: str, sec: str) -> None:
        self.first = fir
        self.second = sec
        self.lift = self.calc_lift(df)

    def calc_lift(self, df: pd.DataFrame) -> float:
        # should return lift of rule if first -> second
        # you can use function calc_prob(df) in Eclat class
        return Eclat.calc_prob(df, [self.first, self.second]) / (Eclat.calc_prob(df, [self.first]) * Eclat.calc_prob(df, [self.second]))

    def calc_conf(self, df: pd.DataFrame) -> float:
        return 0.0
